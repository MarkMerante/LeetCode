#567. Permutation in String

#Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
#In other words, return true if one of s1's permutations is the substring of s2

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1Dic = {}
        s2Dic = {}
        l, r = 0, len(s1)
        
        for char in s1:
            if char in s1Dic:
                s1Dic[char] += 1
            else: 
                s1Dic[char] = 1
        
        while r <= len(s2):
            s2Sub = s2[l:r]
            for char2 in s2Sub:
                if char2 in s2Dic:
                    s2Dic[char2] += 1
                else: 
                    s2Dic[char2] = 1
                    
            if sorted(s1Dic.items()) == sorted(s2Dic.items()):
                return True
            else: 
                s2Dic.clear()
                l += 1
                r += 1
        
        return False