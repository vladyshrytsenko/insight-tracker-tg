from datetime import datetime, timezone

def get_today_date():
    """Get today's date in YYYY-MM-DD format (UTC)."""
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")

def get_date_range_for_today():
    """Get date range for today: since and until."""
    today = get_today_date()
    return today, today