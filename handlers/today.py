from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
import logging

from fb.ads_client import FacebookAdsClient
from services.calculator import GamblingKPICalculator
from ai.analyze import analyze_gambling_stats
from services.formatter import TelegramFormatter

logger = logging.getLogger(__name__)

router = Router()

@router.message(Command("today"))
async def today_handler(message: Message):
    """Handle /today command: fetch, process, and analyze today's stats."""
    try:
        await message.reply("Fetching today's Facebook Ads data...")

        # Fetch raw stats
        client = FacebookAdsClient()
        raw_stats = await client.fetch_today_insights()

        if not raw_stats:
            await message.reply("No data available for today.")
            return

        # Normalize KPIs
        normalized_stats = GamblingKPICalculator.normalize_stats(raw_stats)

        # AI Analysis
        analysis = await analyze_gambling_stats(normalized_stats)

        # Format message
        formatted_message = TelegramFormatter.format_today_performance(normalized_stats, analysis)

        await message.reply(formatted_message)

    except Exception as e:
        logger.error(f"Error in /today handler: {e}")
        await message.reply("An error occurred while processing today's data. Check logs.")
        