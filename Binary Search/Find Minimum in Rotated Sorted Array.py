
# ------------------------------------------------------------------------------------------------------------
# Problem no :  153
# Problem heading :  Find Minimum in Rotated Sorted Array
# Problem Link : https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

# Problem Description : 
#   Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:
#   [4,5,6,7,0,1,2] if it was rotated 4 times.
#   [0,1,2,4,5,6,7] if it was rotated 7 times.
#   Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
#   Given the sorted rotated array nums of unique elements, return the minimum element of this array.
#   You must write an algorithm that runs in O(log n) time.

#  *******************************************************************
#   Input: nums = [3,4,5,1,2]
#   Output: 1
#   Explanation: The minimum element in the array is 1.

#   Input: nums = [4,5,6,7,0,1,2]
#   Output: 0
#   Explanation: The minimum element in the array is 0.
 
#  *******************************************************************

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        min_val = float('inf')
        while(left <= right):
            mid =  left + (right - left) // 2
            
            min_val = min(nums[mid], min_val)

            if(nums[mid]>nums[right]):
                left = mid + 1
            else:
                right = mid - 1
        return min_val