
# ------------------------------------------------------------------------------------------------------------
# Problem no :  724
# Problem heading :  Find Pivot Index
# Problem Link : https://leetcode.com/problems/find-pivot-index/description/

# Problem Description : 
#   Given an array of integers nums, calculate the pivot index of this array.
#   The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the right of the index.

#-------------------------------------------------------------------------------------------------------------

#  *******************************************************************
#   Input: [1,7,3,6,5,6]
#   Output: 3
#   Explanation:
#   The pivot index is 3.
#   Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
#   Right sum = nums[4] + nums[5] = 5 + 6 = 11
#  *******************************************************************

#   Input: nums = [1,2,3]
#   Output: -1

#  Explanation:
#   There is no pivot index in the array.
#  *******************************************************************

class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        totalsum = sum(nums)
        leftsum=0
        ans=0
        completed=False
        for i in range(0,len(nums)):
            rightsum = totalsum - leftsum - nums[i]
            if(leftsum==rightsum):
                ans=i
                completed = True
                break
            leftsum =  leftsum + nums[i]
        if completed == False:
            return -1
        else:
            return ans