# 169. Majority Element

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numsDict = {}
        
        for i in range(len(nums)):
            numsDict[nums[i]] = 1 + numsDict.get(nums[i], 0)
        
        return max(numsDict, key = lambda k : numsDict[k])