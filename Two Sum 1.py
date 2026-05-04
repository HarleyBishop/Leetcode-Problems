
# ? Problem Descriptions:
# ?   Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# ?   You may assume that each input would have exactly one solution, and you may not use the same element twice.
# ?   You can return the answer in any order.




# * Notes: 
#*        Could brute force by looping through for each value causing O(n2) however more efficent to use ernumerate on a hashset. Enumerate returns pairs of values conmtaining bvoth index and value. Just do target - value and check whether the result ot complement exists in the hashset of seen values



# ! SOLUTION 
class Solution(object):
    def twoSum(self, nums, target):
        seen = {}  

        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], i]

            seen[num] = i


    
