from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from utils import get_summary

app = Flask(__name__)


@app.route("/")
def home():
    return "🤖 YouTube Summarizer WhatsApp Bot is running!"

@app.route("/test")
def test():
    return "✅ Webhook endpoint is accessible!"

@app.route("/whatsapp", methods=["POST"])
def whatsapp():
    incoming_msg = request.values.get('Body', '').strip()
    print(f"📨 Received message: {incoming_msg}")
    resp = MessagingResponse()
    msg = resp.message()

    if "youtube.com" in incoming_msg or "youtu.be" in incoming_msg:
        msg.body("⏳ Processing your YouTube link. Please wait...")
        summary = get_summary(incoming_msg)
        msg.body(summary)
    else:
        msg.body("👋 Please send a valid YouTube video link to get a summary.")

    return str(resp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
