# 266. Palindrome Permutation

# Given a string s, return true if a permutation of the string could form a palindrome.

# Example 1:
# Input: s = "code"
# Output: false

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        palDic = {}
        
        for char in s:
            if char in palDic:
                palDic[char] += 1
            else:
                palDic[char] = 1
        
        count = 0
        for key in palDic:
            count += palDic[key] %2
            
        return count <= 1