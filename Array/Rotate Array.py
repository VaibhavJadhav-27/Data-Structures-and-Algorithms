
# ------------------------------------------------------------------------------------------------------------
# Problem no :  189
# Problem heading :  Rotate Array
# Problem Link : https://leetcode.com/problems/rotate-array/description/

# Problem Description : 
#   Given an integer array nums, rotate the array to the right by k steps, where k is non-negative

#-------------------------------------------------------------------------------------------------------------

#  *******************************************************************
#   Input: nums = [1,2,3,4,5,6,7], k = 3
#   Output: [5,6,7,1,2,3,4]
#   Explanation: 
#   rotate 1 steps to the right: [7,1,2,3,4,5,6]
#   rotate 2 steps to the right: [6,7,1,2,3,4,5]
#   rotate 3 steps to the right: [5,6,7,1,2,3,4]
#
#  *******************************************************************


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)

        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])
        