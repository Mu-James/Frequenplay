def validMinMidMax(min_value: int, mid_value: int, max_value: int) -> bool:
    minmid = min_value < mid_value
    midmax = mid_value < max_value
    minmax = min_value < max_value
    
    return minmid and midmax and minmax