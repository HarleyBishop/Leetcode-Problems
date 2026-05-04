
# ? Problem Descriptions:
# ?   Given two strings s and t, return true if t is an anagram of s, and false otherwise.


# * Notes: 
#*        2 Good Solutions. Most efficient is o(n) as shown below solution checks is the stirngs are the same lenght if so count each char in a hashset/dict. Then compare characters in 2nd string to letter stored in count to check they exist and number of times they appear


# ! SOLUTION 
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        count = {}

        for char in s:
            count[char] = count.get(char, 0) + 1

        for char in t:
            if char not in count or count[char] == 0:
                return False 
            count[char] -= 1

        return True


    
