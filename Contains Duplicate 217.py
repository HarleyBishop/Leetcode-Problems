
# ? Problem Descriptions:
# ?   Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.


# * Notes: 
#*        2 Easy solutons one is adding to set one is adding to array and doing the same thing. Set is more efficent and has complexity O(1) as in a set a lookup table can instantly find the value hwereas in an array ther line if num in values causes a complexity of o(n) as every individual vaslue is checked one by one


# ! SOLUTION 
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        values = set()
        for num in nums:
            if (num in values):
                return True
            else:
                values.add(num)

        return False
            
    
