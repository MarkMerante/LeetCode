# 217. Contains Duplicate

# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

#second try
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        duplicateChecker = {}
        for n in nums:
            if n in duplicateChecker:
                return True
            duplicateChecker[n] = n
        
        return False
