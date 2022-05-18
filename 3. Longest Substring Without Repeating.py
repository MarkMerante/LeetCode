# 3. Longest Substring Without Repeating Characters

#Given a string s, find the length of the longest substring without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == " ":
            return 1
        counter = 0
        maxCounter = 0
        for i, val in enumerate(s):
            stop = 0
            if val not in s[stop:i+1]:
                counter += 1
            else:
                if counter > maxCounter:
                    maxCounter = counter
                counter = 1
                stop = i 
                
        return maxCounter