
# ------------------------------------------------------------------------------------------------------------
# Problem no :  219
# Problem heading :  Contains Duplicate II
# Problem Link : https://leetcode.com/problems/contains-duplicate-ii/description/?envType=problem-list-v2&envId=hash-table

# Problem Description : 
#   Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.


#-------------------------------------------------------------------------------------------------------------

#  *******************************************************************
#   Input: nums = [1,2,3,1], k = 3
#   Output: True
#
        #   Explanation: The number 1 appears twice in the array and the absolute difference between their indices is 3.
        #   Note that the array contains duplicates.
#
#  *******************************************************************

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dict1 ={}
        for i in range(0, len(nums)):
            if nums[i] not in dict1:
                dict1[nums[i]] = i
            else:
                j=dict1[nums[i]]
                if(abs(i-j) <= k):
                    return True
                else:
                    dict1[nums[i]] = i
        return False
        