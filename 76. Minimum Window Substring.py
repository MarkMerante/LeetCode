# 76. Minimum Window Substring

# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that 
# every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.
# A substring is a contiguous sequence of characters within the string.

# Example 1:
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        indexQ = deque()
        valQ = deque()
        
        res = []
        for i, n in enumerate(nums):
            while valQ and n > valQ[-1]:
                valQ.pop()
                indexQ.pop()
            valQ.append(n)
            indexQ.append(i)
            
            while i - indexQ[0] + 1 > k:
                valQ.popleft()
                indexQ.popleft()
            if i + 1 >= k:
                res.append(valQ[0])
        return res

