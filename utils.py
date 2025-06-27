from datetime import datetime, timezone

def days_old(dt):
    now = datetime.now(timezone.utc)
    return (now - dt).days
