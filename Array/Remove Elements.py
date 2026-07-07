
# ------------------------------------------------------------------------------------------------------------
# Problem no :  27
# Problem heading :  Remove Element
# Problem Link : https://leetcode.com/problems/remove-element/description/

# Problem Description : 
#   Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
#   The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

#-------------------------------------------------------------------------------------------------------------

#  *******************************************************************
#   Input: nums = [0,1,2,2,3,0,4,2], val = 2
#   Output: 5, nums = [0,1,4,0,3,_,_,_]
#   Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4. 
#   Note that the five elements can be returned in any order. 
#   It does not matter what you leave beyond the returned k (hence they are underscores).
#
#  *******************************************************************


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i=0
        j=0
        while(j <  len(nums)):
            if(nums[j]==val):
                j=j+1
            else:
                nums[i]=nums[j]
                i=i+1
                j=j+1
        return i
        