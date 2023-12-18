from time_conversion import convertMilisTimestamp

def mostReplayedSearch(timestamp_intesnties: list[dict]) -> list:
    """
    Returns a list of timedelta objects representing the most replayed
    timestamp given.
    """
    most_replayed = []

    for timestamp in timestamp_intesnties:
        if timestamp["intensityScoreNormalized"] == 1:
            most_replayed.append(convertMilisTimestamp(timestamp["startMillis"]))

    return most_replayed
