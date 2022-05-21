# 347. Top K Frequent Elements
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        val = {}
        for i in range(len(nums)):
            if nums[i] in val:
                val[nums[i]] += 1
            else:
                val[nums[i]] = 1
        
        frequentList = []
        for i in range(k):
            maxElement = max(val, key=val.get)
            frequentList.append(maxElement)
            val.pop(maxElement)
        
        return frequentList