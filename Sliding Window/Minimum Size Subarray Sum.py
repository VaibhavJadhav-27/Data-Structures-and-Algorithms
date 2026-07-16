
# ------------------------------------------------------------------------------------------------------------
# Problem no :  209
# Problem heading :  Minimum Size Subarray Sum
# Problem Link : https://leetcode.com/problems/minimum-size-subarray-sum/description/

# Problem Description : 
#   Given an array of positive integers and a target sum, find the minimal length of a contiguous subarray with sum at least the target.

#-------------------------------------------------------------------------------------------------------------

#  *******************************************************************
#   Input: target = 7, nums = [2,3,1,2,4,3]
#   Output: 2
#   Explanation: The subarray [4,3] has the minimal length under the problem constraint.

#   Input: target = 4, nums = [1,4,4]
#   Output: 1
#   Explanation: The subarray [4] has the minimal length under the problem constraint.
#  *******************************************************************

class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        window = 0      # first mistake
        minimum_length = float('inf')
        for right in range(len(nums)):
            window = window + nums[right]
            while(window>=target):
                minimum_length =  min(minimum_length,(right-left+1))
                window =  window - nums[left]
                left = left + 1
                
        if minimum_length == float('inf'):
            return 0
        return minimum_length