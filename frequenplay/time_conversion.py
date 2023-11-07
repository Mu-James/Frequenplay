def convertMilis(millis: int) -> tuple[int, int, int]:
    seconds = (millis / 1000) % 60
    minutes = (millis / (1000 * 60)) % 60
    hours = (millis / (1000 * 60 * 60)) % 24
    return (hours, minutes, seconds)