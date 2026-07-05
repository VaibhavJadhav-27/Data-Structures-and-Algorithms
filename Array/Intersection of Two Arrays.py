
# ------------------------------------------------------------------------------------------------------------
# Problem no :  349
# Problem heading :  Intersection of Two Arrays
# Problem Link : https://leetcode.com/problems/intersection-of-two-arrays/description/

# Problem Description : 
#   Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.


#-------------------------------------------------------------------------------------------------------------

#  *******************************************************************
#   Input: nums1 = [1,2,3,1], nums2 = [2,3]
#   Output: [2,3]
#
        #   Explanation: The numbers 2 and 3 are present in both arrays.
        #   Note that the result contains only unique elements.
#
#  *******************************************************************


class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dict1= {}
        ans= []
        for i in nums1:
            if i not in dict1:
                dict1[i] = 0
            else:
                continue
        for i in nums2:
            if i in dict1 and i not in ans:
                ans.append(i)

        return ans