
# ------------------------------------------------------------------------------------------------------------
# Problem no :  169
# Problem heading :  Majority Element
# Problem Link : https://leetcode.com/problems/majority-element/description/

# Problem Description : 
#   Given an array nums of size n, return the majority element.
#   The majority element is the element that appears more than ⌊n / 2⌋ times. 
#   You may assume that the majority element always exists in the array.


#-------------------------------------------------------------------------------------------------------------

#  *******************************************************************
#   Input: nums = [2,2,1,1,1,2,2]
#   Output: 2
#
#   Explanation: It should be 2 as it appears 4 times which is more than n/2 times.
#
#  *******************************************************************

import math

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cutoff = math.floor(len(nums)/2)
        for i in set(nums):
            if(nums.count(i)>cutoff):
                return i
        