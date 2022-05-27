# 56. Merge Intervals

# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
# and return an array of the non-overlapping intervals that cover all the intervals in the input.

# Example 1:
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6]

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
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
