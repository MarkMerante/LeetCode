# 242. Valid Anagram
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sCounter = {}
        tCounter = {}
        
        for i in range(len(s)):
            if s[i] in sCounter:
                sCounter[s[i]]+=1
            else:
                sCounter[s[i]] = 1
            if t[i] in tCounter:
                tCounter[t[i]]+=1
            else:
                tCounter[t[i]] = 1
            
        return (sorted(sCounter.items(), key=lambda x:x[0])) == (sorted(tCounter.items(), key=lambda x:x[0]))