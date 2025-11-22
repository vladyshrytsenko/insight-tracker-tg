import logging
from typing import Dict, Any
from openai import AsyncOpenAI
from config import Config

logger = logging.getLogger(__name__)

async def analyze_gambling_stats(stats: Dict[str, Any]) -> str:
    """Analyze Facebook Ads performance for today's Gambling campaigns using AI."""
    if not stats:
        return "No data available for analysis."

    if not Config.OPENAI_API_KEY:
        return "AI analysis unavailable due to missing API key."

    client = AsyncOpenAI(api_key=Config.OPENAI_API_KEY)

    # Extract stats with defaults to avoid KeyError
    spend = stats.get('spend', 0.0)
    impressions = stats.get('impressions', 0)
    clicks = stats.get('clicks', 0)
    ctr = stats.get('ctr', 0.0)
    cpc = stats.get('cpc', 0.0)
    cpm = stats.get('cpm', 0.0)
    installs = stats.get('installs', 0)
    registrations = stats.get('registrations', 0)
    deposits = stats.get('deposits', 0)
    revenue = stats.get('revenue', 0.0)
    roas = stats.get('roas', 0.0)
    cpi = stats.get('cpi', 0.0)
    cpr = stats.get('cpr', 0.0)
    cpd = stats.get('cpd', 0.0)
    cr_click_install = stats.get('cr_click_install', 0.0)
    cr_install_reg = stats.get('cr_install_reg', 0.0)
    cr_reg_dep = stats.get('cr_reg_dep', 0.0)
    quality_ranking = stats.get('quality_ranking', 'N/A')
    conversion_rate_ranking = stats.get('conversion_rate_ranking', 'N/A')
    engagement_rate_ranking = stats.get('engagement_rate_ranking', 'N/A')

    prompt = f"""
    Analyze the following Facebook Ads performance data for a Gambling (Casino/Betting) campaign today:

    Spend: ${spend:.2f}
    Impressions: {impressions}
    Clicks: {clicks}
    CTR: {ctr:.2%}
    CPC: ${cpc:.2f}
    CPM: ${cpm:.2f}

    Installs: {installs}
    Registrations: {registrations}
    Deposits: {deposits}
    Revenue: ${revenue:.2f}
    ROAS: {roas:.2f}

    CPI: ${cpi:.2f}
    CPR: ${cpr:.2f}
    CPD: ${cpd:.2f}

    Conversion Rates:
    Click → Install: {cr_click_install:.2f}%
    Install → Reg: {cr_install_reg:.2f}%
    Reg → Deposit: {cr_reg_dep:.2f}%

    Rankings:
    Quality: {quality_ranking}
    Conversion Rate: {conversion_rate_ranking}
    Engagement: {engagement_rate_ranking}

    Provide a concise analysis including:
    - Performance summary
    - Funnel analysis
    - KPI benchmarks vs typical Gambling traffic norms
    - Detection of bad indicators (bot clicks, saturation, creative fatigue)
    - Ban-risk indicators
    - Recommendations for optimization (creative, GEO, preland, bid, budget)
    - Warnings about broken funnel steps

    Keep it actionable and Gambling-specific.
    """

    try:
        response = await client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000,
            temperature=0.5,
        )
        analysis = response.choices[0].message.content.strip()
        return analysis
    except Exception as e:
        logger.error(f"AI analysis failed: {e}")
        return "AI analysis unavailable due to error."
    