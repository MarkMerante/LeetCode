# 1. Two Sum
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#You can return the answer in any order..

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sortedNums = sorted(nums)
        newList = []
        for i in sortedNums:
            if target <=  i:
                newList.append(i)
                
        n = 1
        while n < len(newList)+1:
            search = newList[-n] - target
            if search in newList:
                position = newList.index(search)
                return [position, (len(newList) - 1) - n]
            n  += 1