# 219. Contains Duplicate II

# Given an integer array nums and an integer k, return true if there are two distinct indices i 
# and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

# Example 1: 
# Input: nums = [1,2,3,1], k = 3
# Output: true

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        numsDic = {}
        
        for i, j in enumerate(nums):
            if j in numsDic and i - numsDic[j] <= k:
                return True
            numsDic[j] = i
            
        return False