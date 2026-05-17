
# Given a sorted array that has been rotated n times return the minimum value. Solutoin must be O(log N)

# * Notes:  Because the values are unique and the array was previously sorted there has to be 2 sections of the array. 1 section that is sorted normally e.g. [3, 4, 5, 1, 2]  the values 3, 4 and 5 are normally sorted as the left value is less then the right 3 < 5 however 1 and 2 are to the right of 5 
# *  however 1, 2 < 5 so the right side isnt normally sorted therefore the value must be in the right side ofthe array. In another case where its to the left e.g. [5, 1, 2, 3, 4]. 4 is greater then middle point 2 therefore minimum is to the left
# * in Edge case where the array has not been roatted or has been rotated len(nums) times so the array is normal. The solution will still end up with the correct value.


# ! Solution:

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len[nums] - 1

        while l < r:
            m = (l + r) // 2

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        return nums[l]