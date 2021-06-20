# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self[0] = s
        self[1] = e

class Solution:

    def overlaps(self, interval, new_interval):
        if interval[0] < new_interval[0] and interval[1] < new_interval[0]:
            return False
        if interval[0] > new_interval[0] and interval[1] > new_interval[1]:
            return False
            
        return True

    # @param intervals, a list of Intervals
    # @param new_interval, a Interval
    # @return a list of Interval
    def insert(self, intervals, new_interval):
        merged_intervals = []
        overlapped = False
        if not intervals:
            return [new_interval]
        elif new_interval[1] < intervals[0][0]:
            return [new_interval]+intervals
        elif new_interval[0] > intervals[-1][1]:
            return intervals+[new_interval]
        
        for i, interval in enumerate(intervals):
            if Solution().overlaps(interval, new_interval):
                new_interval[0] = min(new_interval[0], interval[0])
                new_interval[1] = max(new_interval[1], interval[1])
                overlapped = True
            else:
                if not overlapped and new_interval[0] > interval[1]:
                    merged_intervals.append(interval)
                else:
                    break
                
        merged_intervals += new_interval,
        if merged_intervals[-1][1] < intervals[i][0]:
            merged_intervals += intervals[i:]
        
        return merged_intervals



print(Solution().insert([[1,3],[6,9]], [2,5]))


