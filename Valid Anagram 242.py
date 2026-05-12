
# ? Problem Descriptions:
# ?   Given two strings s and t, return true if t is an anagram of s, and false otherwise.


# * Notes: 
#*        Solution 1 is easy but not the most effective using sorted to check whether both strings are the same when sorted alphabetically however the solution is not the most efficent due to needing to sort being O(nlogn)
#*        Solution 2 is very similar in amoount of code however counter() is a function that maps the valuesi n a string to a dictionary object with each character in a string as the key and the count of each character as the value


# ! SOLUTION 
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        return sorted(s) == sorted(t)
    

# ! BETTER SOLUTION
from collections import Counter
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        return Counter(s) == Counter(t)



    
