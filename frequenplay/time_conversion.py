from datetime import timedelta

def convertMilisTimestamp(ms: int) -> timedelta:
    timestamp = timedelta(milliseconds=ms)
    return timestamp