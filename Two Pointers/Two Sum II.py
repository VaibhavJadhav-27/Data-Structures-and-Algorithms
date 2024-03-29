# ------------------------------------------------------------------------------------------------------------
# Problem no :  125
# Problem heading :  Two Sum II - Input Array is sorted
# Problem Link : https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

# Problem Description : 
#   Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, 
#   find two numbers such that they add up to a specific target number. 
# 
#   Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length. 
#   Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

#-------------------------------------------------------------------------------------------------------------

#  *******************************************************************
#   Input: numbers = [2,7,11,15], target = 9
#   Output: [1,2]
#   Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
#   
#  *******************************************************************

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i=0
        j=len(nums)-1
        while i<j:
            if nums[i]+nums[j]==target:
                return [i+1,j+1]
            elif nums[i]+nums[j]>target:
                j-=1
            else :
                i+=1
        return []