
# ------------------------------------------------------------------------------------------------------------
# Problem no :  704
# Problem heading :  Binary Search
# Problem Link : https://leetcode.com/problems/binary-search/description/

# Problem Description : 
#   Given an array of integers nums which is sorted in ascending order, and an integer target,
#   write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

#  *******************************************************************
#   Input: nums = [-1,0,3,5,9,12], target = 9
#   Output: 4
#   Explanation: 9 exists in nums and its index is 4.

#   Input: nums = [-1,0,3,5,9,12], target = 2
#   Output: -1
#   Explanation: 2 does not exist in nums so return -1.
 
#  *******************************************************************

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while(left  <= right):
            mid = left + (right - left) // 2

            if(nums[mid]==target):
                return mid
            elif(nums[mid]> target):
                right = mid - 1
            else:
                left = mid + 1
        return -1
        