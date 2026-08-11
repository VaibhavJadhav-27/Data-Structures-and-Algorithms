
# ------------------------------------------------------------------------------------------------------------
# Problem no :  34
# Problem heading :  Find First and Last Position of Element in Sorted Array
# Problem Link : https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/

# Problem Description : 
#   Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
#   If target is not found in the array, return [-1, -1].
#   You must write an algorithm with O(log n) runtime complexity.

#  *******************************************************************
#   Input: nums = [5,7,7,8,8,10], target = 8
#   Output: [3, 4]
#   Explanation: The first 8 is at index 3 and the last 8 is at index 4.

#   Input: nums = [5,7,7,8,8,10], target = 6
#   Output: [-1, -1]
#   Explanation: 6 does not exist in nums so return [-1, -1].
 
#  *******************************************************************
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(nums) - 1
        ans1 = -1
        while (left <= right):
            mid = left + (right - left) // 2

            if(nums[mid]==target):
                ans1 = mid
                right =  mid - 1

            elif(nums[mid] > target):
                right = mid - 1
            else:
                left = mid + 1


        left = 0
        right = len(nums) - 1
        ans2 = -1
        while (left <= right):
            mid = left + (right - left) // 2

            if(nums[mid]==target):
                ans2 = mid
                left =  mid + 1

            elif(nums[mid] > target):
                right = mid - 1
            else:
                left = mid + 1
        return [ans1, ans2]
