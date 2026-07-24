
# ------------------------------------------------------------------------------------------------------------
# Problem no :  53
# Problem heading :  Maximum Subarray
# Problem Link : https://leetcode.com/problems/maximum-subarray/description/

# Problem Description : 
#   Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.


#-------------------------------------------------------------------------------------------------------------

#  *******************************************************************
#   Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
#   Output: 6

#   Input: nums = [1]
#   Output: 1

#  Explanation:
#   Using Kadane's algorithm to find the maximum sum of a contiguous subarray.
#  *******************************************************************

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        currSum = nums[0]
        maxSum = nums[0]
        for i in range(1,len(nums)):
            currSum = max(nums[i], currSum + nums[i])
            maxSum =  max(maxSum, currSum)
        return maxSum