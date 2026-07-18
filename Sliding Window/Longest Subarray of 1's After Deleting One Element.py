
# ------------------------------------------------------------------------------------------------------------
# Problem no :  1493
# Problem heading :  Longest Subarray of 1's After Deleting One Element
# Problem Link : https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/description/

# Problem Description : 
#   Given a binary array nums, you should delete one element from it.
#   Return the size of the longest non-empty subarray containing only 1's in the resulting array.
#   Return 0 if there is no such subarray.

#-------------------------------------------------------------------------------------------------------------

#  *******************************************************************
#   Input: nums = [1,1,0,1]
#   Output: 3
#
        #   Explanation: We can delete the 0 at index 2 to get [1,1,1].
        #   The longest subarray of 1's is of length 3.

#  *******************************************************************

#   Input: nums = [0,1,1,1,0,1,1,0,1]
#   Output: 5
#
#   Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1]..
#
#  *******************************************************************


class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left=0
        longest_subarray = 0
        is_zero_deleted=0
        for right in range(len(nums)):
            if(nums[right]==0):
                is_zero_deleted =  is_zero_deleted + 1
            
            while(is_zero_deleted>1):
                if(nums[left]==0):
                    is_zero_deleted = is_zero_deleted - 1
                left = left + 1
            
            longest_subarray = max(longest_subarray, right-left)
        return longest_subarray
