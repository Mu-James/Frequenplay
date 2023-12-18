from time_conversion import convertMilisTimestamp

def sortTimestamps(timestamp_intesnties: list[dict]) -> tuple(list, list):
    """
    Returns a tuple of list of timedelta objects.
    The first list contains most replayed timestamps. A timestamps is the most replayed if it has a normalized intensity score equal to 1.
    The second list contains  other timestamps that have a normalized intensity score less than 1.
    """
    most_replayed = []
    other = []

    for timestamp in timestamp_intesnties:
        if timestamp["intensityScoreNormalized"] == 1:
            most_replayed.append(convertMilisTimestamp(timestamp["startMillis"]))
        else:
            other.append(convertMilisTimestamp(timestamp["startMillis"]))

    return (most_replayed, other)
