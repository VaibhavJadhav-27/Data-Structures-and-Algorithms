# ------------------------------------------------------------------------------------------------------------
# Problem no :  268
# Problem heading :  Missing Number
# Problem Link : https://leetcode.com/problems/missing-number/description/

# Problem Description : 
#   Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

#-------------------------------------------------------------------------------------------------------------

#  *******************************************************************
#   Input: nums = [3,0,1]
#   Output: 2
#   Explanation: The missing number in the range [0, 3] is 2.
#   
#  *******************************************************************


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x= 0
        for i in nums:
            x= x^i
        y=0
        for i in range(0,len(nums)+1):
            y = y ^ i
        return x ^ y