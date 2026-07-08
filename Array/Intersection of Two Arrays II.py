
# ------------------------------------------------------------------------------------------------------------
# Problem no :  350
# Problem heading :  Intersection of Two Arrays II
# Problem Link : https://leetcode.com/problems/intersection-of-two-arrays-ii/description/

# Problem Description : 
#   Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.


#-------------------------------------------------------------------------------------------------------------

#  *******************************************************************
#   Input: nums1 = [1,2,3,1], nums2 = [2,3]
#   Output: [2,3]
#
#   Explanation: The numbers 2 and 3 are present in both arrays.
#   

#   Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
#   Output: [4,9]
#   Explanation: [9,4] is also accepted.
#
#  *******************************************************************

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dict1={}
        ans=[]
        for i in nums1:
            if(i not in dict1):
                dict1[i]=1
            else:
                dict1[i] = dict1[i] + 1

        for i in nums2:
            if(i in dict1 and dict1[i]>0):
                dict1[i]= dict1[i]-1
                ans.append(i)
        return ans
