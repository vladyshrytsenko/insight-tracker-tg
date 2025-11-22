import aiohttp
import json
import logging
import ssl
import certifi
from typing import Dict, Any
from config import Config
from utils.dates import get_date_range_for_today

logger = logging.getLogger(__name__)

class FacebookAdsClient:
    BASE_URL = "https://graph.facebook.com/v19.0"

    def __init__(self):
        self.access_token = Config.FB_ACCESS_TOKEN
        self.ad_account_id = Config.FB_AD_ACCOUNT_ID

    async def fetch_today_insights(self) -> Dict[str, Any]:
        """Fetch today's insights from Facebook Ads API."""
        since, until = get_date_range_for_today()
        url = f"{self.BASE_URL}/act_{self.ad_account_id}/insights"
        params = {
            "access_token": self.access_token,
            "fields": "spend,impressions,clicks,ctr,cpc,cpm,actions,action_values,cost_per_action_type",
            "time_range": json.dumps({"since": since, "until": until}),
            "level": "account",
        }

        timeout = aiohttp.ClientTimeout(total=30)
        ssl_context = ssl.create_default_context(cafile=certifi.where())
        connector = aiohttp.TCPConnector(ssl=ssl_context)
        async with aiohttp.ClientSession(connector=connector, timeout=timeout) as session:
            async with session.get(url, params=params) as response:
                if response.status != 200:
                    logger.error(f"FB API error: {response.status} - {await response.text()}")
                    raise Exception(f"Failed to fetch insights: {response.status}")
                data = await response.json()
                if not data.get("data") or len(data["data"]) == 0:
                    logger.warning("No data returned from FB API")
                    return {}
                # Assuming one entry
                return data["data"][0]
            