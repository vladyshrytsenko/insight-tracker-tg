# Gambling Traffic Analytics Telegram Bot

A Telegram bot for analyzing Facebook Ads performance in the gambling (casino/betting) vertical. Fetches today's stats, normalizes KPIs, and provides AI-powered insights.

## Features

- Fetch today's Facebook Ads insights
- Normalize raw data into gambling-specific KPIs (CPI, CPR, CPD, ROAS, etc.)
- AI analysis using OpenAI for actionable recommendations
- Clean Telegram interface with formatted reports

## Project Structure

```
bot/
├── main.py              # Entry point
├── config.py            # Configuration management
├── handlers/
│   ├── start.py         # /start command handler
│   └── today.py         # /today command handler
├── fb/
│   └── ads_client.py    # Facebook Ads API client
├── ai/
│   └── analyze.py       # AI analysis module
├── services/
│   ├── calculator.py    # KPI normalization
│   └── formatter.py     # Telegram message formatting
├── utils/
│   └── dates.py         # Date utilities
├── requirements.txt     # Python dependencies
├── .env.example         # Environment variables template
└── README.md
```

## Setup

### 1. Clone and Install Dependencies

```bash
cd bot
pip install -r requirements.txt
```

### 2. Environment Configuration

Copy `.env.example` to `.env` and fill in your credentials:

```bash
cp .env.example .env
```

Edit `.env`:

```
TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
FB_AD_ACCOUNT_ID=your_facebook_ad_account_id_here
FB_ACCESS_TOKEN=your_facebook_access_token_here
OPENAI_API_KEY=your_openai_api_key_here
```

### 3. Create Telegram Bot

1. Message [@BotFather](https://t.me/botfather) on Telegram
2. Use `/newbot` command
3. Follow instructions to get your bot token
4. Paste token into `.env`

### 4. Facebook Ads API Setup

1. Go to [Facebook Developers](https://developers.facebook.com/)
2. Create an app or use existing one
3. Add Marketing API product
4. Generate access token with `ads_read` permission
5. Get your Ad Account ID from Business Manager
6. Paste into `.env`

### 5. OpenAI API Key

1. Go to [OpenAI Platform](https://platform.openai.com/)
2. Create API key
3. Paste into `.env`

## Running the Bot

```bash
python main.py
```

The bot will start polling for messages.

## Usage

- `/start` - Welcome message and instructions
- `/today` - Get today's performance analysis

## Deployment

### Local

Just run `python main.py` in a screen/tmux session or use systemd.

### Server

For production, consider:

- Docker container
- VPS with systemd service
- Cloud functions (AWS Lambda, etc.)

Example systemd service:

```ini
[Unit]
Description=Gambling Analytics Bot

[Service]
Type=simple
User=youruser
WorkingDirectory=/path/to/bot
ExecStart=/usr/bin/python3 main.py
Restart=always

[Install]
WantedBy=multi-user.target
```

## API Details

- **Facebook API**: v19.0, Insights endpoint
- **OpenAI**: GPT-3.5-turbo for analysis
- **Telegram**: aiogram 3.x

## Error Handling

- Logs errors to console
- Validates config on startup
- Handles API failures gracefully

## Security Notes

- Never commit `.env` file
- Use strong API keys
- Limit Facebook token permissions to read-only