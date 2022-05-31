# 125. Valid Palindrome

# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters 
# and removing all non-alphanumeric characters, it reads the same forward and backward. 
# Alphanumeric characters include letters and numbers

# Given a string s, return true if it is a palindrome, or false otherwise.

# Example 1:
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        reverse = s[::-1].lower()
        s2 = s.lower()
        reversedString = " ".join(filter(lambda x:x.isalnum(), reverse)).replace(" ","")
        s2Reverse = " ".join(filter(lambda x:x.isalnum(), s2)).replace(" ","")
        return reversedString == s2Reverse