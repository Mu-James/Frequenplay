from time_conversion import convertMilisTimestamp

def sortTimestamps(timestamp_intesnties: list[dict]) -> ((list, int), (list, int)):
    """
    Returns a tuple of two tuples each with a list of timedelta objects and the number of entries.
    The first list contains most replayed timestamps. A timestamps is the most replayed if it has a normalized intensity score equal to 1.
    The second list contains  other timestamps that have a normalized intensity score less than 1.
    """
    most_replayed = []
    mr_entries = 0
    other = []
    o_entries = 0

    for timestamp in timestamp_intesnties:
        if timestamp["intensityScoreNormalized"] == 1:
            most_replayed.append(convertMilisTimestamp(timestamp["startMillis"]))
            mr_entries += 1
        else:
            other.append(convertMilisTimestamp(timestamp["startMillis"]))
            o_entries += 1

    return ((most_replayed, mr_entries), (other, o_entries))
