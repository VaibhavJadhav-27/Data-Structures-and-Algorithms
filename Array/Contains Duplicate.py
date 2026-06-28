
# ------------------------------------------------------------------------------------------------------------
# Problem no :  217
# Problem heading :  Contains Duplicate
# Problem Link : https://leetcode.com/problems/contains-duplicate/description/

# Problem Description : 
#   Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.


#-------------------------------------------------------------------------------------------------------------

#  *******************************************************************
#   Input: nums = [1,2,3,1]
#   Output: True
#
        #   Explanation: The number 1 appears twice in the array.
        #   Note that the array contains duplicates.
#
#  *******************************************************************

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dict1= {}
        for i in nums:
            if i not in dict1:
                dict1[i] = 1
            else:
                return True
        return False
        