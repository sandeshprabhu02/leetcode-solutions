# Definition for an interval.
# class Interval:
#     def __init__[self, s=0, e=0]:
#         self[0] = s
#         self[1] = e

class Solution:
    # @param intervals, a list of Intervals
    # @param new_interval, a Interval
    # @return a list of Interval
    def insert(self, intervals):
        merged_interval=[]
        for interval in sorted(intervals, key= lambda i:i[0]):
            print(interval[0], interval[1])
            if len(merged_interval) > 0 and merged_interval[-1][1] >= interval[0]:
                merged_interval[-1][1] = max(merged_interval[-1][1], interval[1])
            else:
                merged_interval.append(interval)
        return merged_interval



print(Solution().insert([[1, 10], [2, 9], [3, 8], [4, 7], [5, 6], [6, 6]]))


# a= [ (1, 10), (2, 9), (3, 8), (4, 7), (5, 6), (6, 6) ]


# The expected return value: 
# (1, 10) 