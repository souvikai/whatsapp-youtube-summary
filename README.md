
# YouTube Video Summarizer WhatsApp Bot

A Flask-based WhatsApp bot that generates AI-powered summaries of YouTube videos using OpenAI's GPT-4 and provides clickable timestamps.

## Features

- 🎯 **AI-Powered Summaries**: Get TL;DR summaries of YouTube videos
- 📌 **Clickable Timestamps**: Navigate to specific video moments
- 💬 **WhatsApp Integration**: Send YouTube links via WhatsApp and receive summaries
- ⚡ **Fast Processing**: Efficient transcript extraction and summarization

## Prerequisites

- Python 3.11+
- OpenAI API key
- Twilio account with WhatsApp sandbox access

## Setup

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd youtube-summarizer-bot
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Environment Configuration**
   - Copy `.env.example` to `.env`
   - Fill in your API keys and credentials:
     ```
     OPENAI_API_KEY=your_openai_api_key_here
     TWILIO_ACCOUNT_SID=your_twilio_account_sid_here
     TWILIO_AUTH_TOKEN=your_twilio_auth_token_here
     ```

4. **Run the application**
   ```bash
   python main.py
   ```

## Usage

1. Send a YouTube video URL to your configured WhatsApp number
2. The bot will process the video and return:
   - A TL;DR summary
   - 5 key highlights with clickable timestamps
   - Quick navigation links to important moments

## API Endpoints

- `POST /whatsapp` - Webhook endpoint for Twilio WhatsApp messages

## Deployment

This application is configured for deployment on Replit with the following files:
- `Procfile` - Defines the web process
- `runtime.txt` - Specifies Python version
- `requirements.txt` - Lists all dependencies

## Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `OPENAI_API_KEY` | Your OpenAI API key | Yes |
| `TWILIO_ACCOUNT_SID` | Twilio Account SID | Yes |
| `TWILIO_AUTH_TOKEN` | Twilio Auth Token | Yes |
| `TWILIO_WHATSAPP_NUMBER` | Twilio WhatsApp number | Optional |

## Error Handling

The bot handles various error scenarios:
- Invalid YouTube URLs
- Videos without transcripts
- API rate limiting
- Network connectivity issues

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).
