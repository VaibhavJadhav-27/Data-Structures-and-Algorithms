
# ------------------------------------------------------------------------------------------------------------
# Problem no :  303
# Problem heading :  Range Sum Query - Immutable
# Problem Link : https://leetcode.com/problems/range-sum-query-immutable/description/

# Problem Description : 
#   Given an integer array nums, handle multiple queries of the following type:

#   Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.

#   Implement the NumArray class:
#   NumArray(int[] nums) Initializes the object with the integer array nums.
#   int sumRange(int left, int right) Returns the sum of the elements of nums

#-------------------------------------------------------------------------------------------------------------

#  *******************************************************************
#   Input: ["NumArray", "sumRange", "sumRange", "sumRange"]
#   [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
#   Output: [null, 1, -1, -3]

#  Explanation:
#   NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
#   numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
#   numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
#   numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3

#  *******************************************************************

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums=nums

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        res=0
        for i in range(left, right+1):
            res = res + self.nums[i]
        return res


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)