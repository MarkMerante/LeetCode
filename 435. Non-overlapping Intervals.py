# 435. Non-overlapping Intervals

# Given an array of intervals intervals where intervals[i] = [starti, endi], 
# return the minimum number of intervals you need to remove to make the 
# rest of the intervals non-overlapping.

# Example 1:
# Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
# Output: 1
# Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Did not solve Leetcode of the day