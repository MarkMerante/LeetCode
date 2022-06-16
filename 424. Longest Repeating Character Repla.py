# 424. Longest Repeating Character Replacement

#You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.
#Return the length of the longest substring containing the same letter you can get after performing the above operations.

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charSet = set()
        maxChar = 0
        left, right = 0, 1
        
        while right < len(s):
            if len(charSet) > k:
                left += 1
        # To be continued
            
