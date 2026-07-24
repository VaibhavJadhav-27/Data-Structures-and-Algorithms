
# ------------------------------------------------------------------------------------------------------------
# Problem no :  1480
# Problem heading :  Running Sum of 1d Array
# Problem Link : https://leetcode.com/problems/running-sum-of-1d-array/description/

# Problem Description : 
#   Given an array of integers nums, calculate the running sum of the array.

#   We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]). 

#-------------------------------------------------------------------------------------------------------------

#  *******************************************************************
#   Input: nums = [1,2,3,4]
#   Output: [1,3,6,10]

#   Input: nums = [1,1,1,1,1]
#   Output: [1,2,3,4,5]

#  *******************************************************************

class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans=[]
        ans.append(nums[0])
        for i in range(1,len(nums)):
            ans.append((nums[i]+ans[i-1]))
        return ans
        