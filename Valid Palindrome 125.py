# ? Problem Descriptions:
# ?   A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers Given a string s, return true if it is a palindrome, or false otherwise.


# * Notes: 
#*        2 Very good solutions. The one below is the more inefficent in terms of space complexity however is easier to understand. The trick for the space efficiency is how alphanumeric numbers are checked as the current solution uses an extra string variable to store the new string


# ! SOLUTION 
class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = ""
        
        for c in s:
            if c.isalnum():
                new += c.lower()
        
        return new == new[::-1]



