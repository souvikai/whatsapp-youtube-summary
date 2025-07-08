
import openai
import re
import os
from youtube_transcript_api._api import YouTubeTranscriptApi

openai.api_key = os.getenv("OPENAI_API_KEY")


def get_video_id(url):
    match = re.search(r"(?:v=|youtu.be/)([\w-]+)", url)
    return match.group(1) if match else None


def generate_clickable_timestamps(transcript, video_id, interval=120):
    highlights = []
    for i in range(0, len(transcript), interval):
        start = transcript[i]['start']
        text = transcript[i]['text']
        mins, secs = divmod(int(start), 60)
        timestamp = f"{mins:02}:{secs:02}"
        link = f"https://www.youtube.com/watch?v={video_id}&t={int(start)}s"
        highlights.append(f"- [{timestamp}]({link}) — {text}")
    return highlights[:5]


def get_summary(youtube_url):
    try:
        video_id = get_video_id(youtube_url)
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        full_text = " ".join([t['text'] for t in transcript[:100]])

        prompt = f"Summarize the following YouTube video transcript in a TL;DR and 5 key highlights with timestamps:\n\n{full_text}"
        response = openai.ChatCompletion.create(model="gpt-4",
                                                messages=[{
                                                    "role": "user",
                                                    "content": prompt
                                                }])

        summary = response['choices'][0]['message']['content']
        highlights = generate_clickable_timestamps(transcript, video_id)

        return f"🎯 *TL;DR + Highlights*\n\n{summary}\n\n📌 *Clickable Timestamps*\n" + "\n".join(
            highlights)

    except Exception as e:
        return f"⚠️ Error: {str(e)}"
