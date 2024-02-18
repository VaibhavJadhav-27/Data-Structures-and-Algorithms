
# ------------------------------------------------------------------------------------------------------------
# Problem no :  26
# Problem heading :  Remove Duplicate from Sorted Array
# Problem Link : https://leetcode.com/problems/remove-duplicates-from-sorted-array/

# Problem Description : 
#   Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. 
#   The relative order of the elements should be kept the same. 
#   Then return the number of unique elements in nums.

#-------------------------------------------------------------------------------------------------------------

#  *******************************************************************
#   Input : nums = [1,1,2]
#   Output : 2, nums = [1,2,_]
#   Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively. 
#   It does not matter what you leave beyond the returned k (hence they are underscores).
#
#  *******************************************************************


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums)>0 and len(nums)<2):
            return len(nums)
        i = 0
        j=i+1
        unique = 1
        while(j<len(nums)):
            if(nums[i]==nums[j]):
                j=j+1
                continue
            
            if(nums[i]<nums[j]):
                i=i+1
                nums[i]=nums[j]
                j=j+1
                unique = unique+1
        return unique

        