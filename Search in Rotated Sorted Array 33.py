

#! SOLUTION:

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1

        while left < right:
            middle = (left + right) // 2

            # Return if value is found
            if target == nums[middle]:
                return middle

            # Left half sorted
            if nums[middle] > nums[right]:
                
                # If the target is in the range of the left side 
                if nums[left] <= target < nums[middle]:
                    right = middle
                else:
                    left = middle + 1
            
            else:
                # If in the range of the right side
                if nums[middle] < target <= nums[right]:
                    left = middle
                else:
                    right = middle - 1
        
        # return if target not in array
        return -1








        
