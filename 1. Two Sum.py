# 1. Two Sum
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#You can return the answer in any order..

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # val -> index
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
            #Review of TwoSum
