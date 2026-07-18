
# ------------------------------------------------------------------------------------------------------------
# Problem no :  1004
# Problem heading :  Max Consecutive Ones III
# Problem Link : https://leetcode.com/problems/max-consecutive-ones-iii/description/

# Problem Description : 
#   Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.


#-------------------------------------------------------------------------------------------------------------

#  *******************************************************************
#   Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
#   Output: 6
#
#   Explanation: Flip the two middle 0's to get [1,1,1,1,1,1,1,1,1,1,0], which has 6 consecutive 1's.
#
#  *******************************************************************

class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left=0
        right=0
        zero_count=0
        max_size = 0
        for right in range(len(nums)):
            if(nums[right]==0):
                zero_count =  zero_count + 1
            while(zero_count > k):
                if(nums[left]==0):
                    zero_count = zero_count - 1
                left =  left + 1
            max_size =  max(max_size, right-left+1)
        return max_size
        

        