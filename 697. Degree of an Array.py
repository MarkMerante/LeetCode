# 697. Degree of an Array

# Given a non-empty array of non-negative integers nums, the degree of this array 
# is defined as the maximum frequency of any one of its elements.

# Your task is to find the smallest possible length of a (contiguous) 
# subarray of nums, that has the same degree as nums.

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        numsFrequency = {}
        currentMin = [float('inf')]
        l, r = 0, 0
        
        for i in nums:
            numsFrequency[i] = 1 + numsFrequency.get(i, 0)
        
        maxFrequency = max(numsFrequency, key=numsFrequency.get)
        
        
        if r < len(nums):