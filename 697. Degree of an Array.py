# 697. Degree of an Array

# Given a non-empty array of non-negative integers nums, the degree of this array 
# is defined as the maximum frequency of any one of its elements.

# Your task is to find the smallest possible length of a (contiguous) 
# subarray of nums, that has the same degree as nums.
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        if nums is None:
            return 0
        
        numsFrequency = {}
        l = 0
        r = l 
        
        for i in nums:
            numsFrequency[i] = 1 + numsFrequency.get(i, 0)
        
        maxFrequency = max(numsFrequency, key=numsFrequency.get)
        
        
        while l < len(nums):
            if nums[l] == maxFrequency:
                break
            else:
                l +=1 
        
        while r < len(nums):
            if nums[r] == maxFrequency:
                currentR = r
                shortArray = nums[l:currentR]
            else:
                r+=1
        
        return len(shortArray[l:currentR]) + 1
