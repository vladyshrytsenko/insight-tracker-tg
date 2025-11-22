import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    FB_AD_ACCOUNT_ID = os.getenv("FB_AD_ACCOUNT_ID")
    FB_ACCESS_TOKEN = os.getenv("FB_ACCESS_TOKEN")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    @classmethod
    def validate(cls):
        required_vars = {
            "TELEGRAM_BOT_TOKEN": cls.TELEGRAM_BOT_TOKEN,
            "FB_AD_ACCOUNT_ID": cls.FB_AD_ACCOUNT_ID,
            "FB_ACCESS_TOKEN": cls.FB_ACCESS_TOKEN,
            "OPENAI_API_KEY": cls.OPENAI_API_KEY,
        }
        missing = [name for name, value in required_vars.items() if not value]
        if missing:
            raise ValueError(f"Missing required environment variables: {', '.join(missing)}. Check .env file.")