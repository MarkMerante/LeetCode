# 268. Missing Number

# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i = 0
        
        while i < len(nums):
            if i in nums:
                i += 1
            else:
                return i
        
        return len(nums)