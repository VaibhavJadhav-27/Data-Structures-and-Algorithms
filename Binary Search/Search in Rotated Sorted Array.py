
# ------------------------------------------------------------------------------------------------------------
# Problem no :  33
# Problem heading :  Search in Rotated Sorted Array
# Problem Link : https://leetcode.com/problems/search-in-rotated-sorted-array/description/

# Problem Description : 
#   There is an integer array nums sorted in ascending order (with distinct values).
#   Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
#   Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

#  *******************************************************************
#   Input: nums = [4,5,6,7,0,1,2], target = 0
#   Output: 4
#   Explanation: 0 exists in nums and its index is 4.

#   Input: nums = [4,5,6,7,0,1,2], target = 3
#   Output: -1
#   Explanation: 3 does not exist in nums so return -1.
 
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
        while(left <= right):
            mid =  left + (right - left) // 2

            if(nums[mid]==target):
                return mid

            if(nums[left]<= nums[mid]):  
                ## left half is sorted  
                if(nums[left]<=target and nums[mid] >target):
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                ##  right half is sorted
                if(nums[mid] < target and nums[right]>=target):
                    left = mid + 1
                else:
                    right = mid - 1
        return -1  