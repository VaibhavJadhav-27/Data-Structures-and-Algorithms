
# ------------------------------------------------------------------------------------------------------------
# Problem no :  283
# Problem heading :  Move Zeros
# Problem Link : https://leetcode.com/problems/move-zeroes/description/

# Problem Description : 
#   Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#   Note that you must do this in-place without making a copy of the array.


#-------------------------------------------------------------------------------------------------------------

#  *******************************************************************
#   Input: nums = [0,1,0,3,12]
#   Output: [1,3,12,0,0]
#
#   Explanation: It should be [1,3,12,0,0] after calling your function. 
#
#  *******************************************************************


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i=0
        j=1
        if(len(nums)==1):
            return nums
        
        while(j<len(nums)):
            if(nums[i]==0 and nums[j]!=0):
                nums[i],nums[j] = nums[j], nums[i]
                i=i+1
                j=j+1
            
            elif(nums[i]==0 and nums[j]==0):
                j=j+1
            
            elif(nums[i]!=0):
                i=i+1
                j=j+1
        
        return nums