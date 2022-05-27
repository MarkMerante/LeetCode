# 57. Insert Interval

# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] 
# represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. 
# You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

# Insert newInterval into intervals such that intervals is still sorted in ascending order 
# by starti and intervals still does not have any overlapping intervals 
# (merge overlapping intervals if necessary).

# Example 1:
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key = lambda pair : pair[0]) #sorts value
        output = [intervals[0]] # gets first array within matrix/2D array
        
        for start, end in intervals:
            lastEnd = output[-1][1] # gets last element from previous array
            
            # if the current starting element from current array is less than
            # or equal to the last element from previous array
            if start <= lastEnd:  
                # merge
                # we update the the previous array and take the max of previous ending element
                # to the current ending element
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end]) # else, we append the array to the matrix/2d array
        return output