# 167. Two Sum II

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numbers.sort()
        
        for i in range(len(numbers)):
            l, r = i, len(numbers) - 1
            while l < r:
                twoSum = numbers[l] + numbers[r]
                if twoSum == target:
                    return [l + 1, r + 1]
                elif twoSum > target:
                    r -= 1
                else:
                    l += 1