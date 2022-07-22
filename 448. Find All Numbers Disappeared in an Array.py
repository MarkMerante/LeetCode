# 448. Find All Numbers Disappeared in an Array

# Given an array nums of n integers where nums[i] is in the range [1, n], 
# return an array of all the integers in the range [1, n] that do not appear in nums.

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        intRange = list(range(1,len(nums)+1))
        missing = []
        numsSet = set(nums)
        
        for i in intRange:
            if i not in numsSet:
                missing.append(i)
        
        return missing