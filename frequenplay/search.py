from time_conversion import convertMilisTimestamp

def mostReplayedSearch(timestamp_intesnties: list[dict]) -> tuple[int, int, int]:
    """
    Returns a timedelta object representing the most replayed
    timestamp given.
    """
    
    for timestamp in timestamp_intesnties:
        if timestamp["intensityScoreNormalized"] == 1:
            return convertMilisTimestamp(timestamp["startMillis"])
    else:
        return None