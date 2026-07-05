
# ------------------------------------------------------------------------------------------------------------
# Problem no :  229
# Problem heading :  Majority Element II
# Problem Link : https://leetcode.com/problems/majority-element-ii/description/

# Problem Description : 
#   Given an integer array of size n, return all elements that appear more than ⌊ n/3 ⌋ times.


#-------------------------------------------------------------------------------------------------------------

#  *******************************************************************
#   Input: nums = [3,2,3]
#   Output: [3]
#
        #   Explanation: The number 3 appears more than ⌊ 3/3 ⌋ = 1 time.
#
#  *******************************************************************


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dict1={}
        ans=[]
        for i in nums:
            if i not in dict1:
                dict1[i]= 1
            else:
                x= dict1[i]
                dict1[i] = x + 1
            if(dict1[i]> (len(nums)/3)):
                if(i not in ans):
                    ans.append(i)
        return ans
        