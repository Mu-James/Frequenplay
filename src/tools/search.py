import time_converstion as tc

def mostReplayedSearch(timestamp_intesnties: list[dict]) -> tuple(int, int, int):
    for timestamp in timestamp_intesnties:
        if timestamp["intensityScoreNormalized"] == 1:
            return tc.convertMilis(timestamp["startMillis"])
    else:
        return None