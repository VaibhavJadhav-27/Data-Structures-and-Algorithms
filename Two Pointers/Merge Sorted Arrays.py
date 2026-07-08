# ------------------------------------------------------------------------------------------------------------
# Problem no :  88
# Problem heading :  Merge Sorted Arrays
# Problem Link : https://leetcode.com/problems/merge-sorted-array/description/

# Problem Description :
#   You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively. Merge nums1 and nums2 into a single array sorted in non-decreasing order.

#-------------------------------------------------------------------------------------------------------------

#  *******************************************************************
#   Example 1:
#   Input:  nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
#   Output: [1,2,2,3,5,6]
#   Explanation: The merged array is [1,2,2,3,5,6].
#
#   Example 2:
#   Input:  nums1 = [1], m = 1, nums2 = [], n = 0
#   Output: [1]
#   Explanation: The merged array is [1].
#  *******************************************************************

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        temp =  nums1 + nums2
        temp.sort()
        print(temp)
        temp = temp[len(nums1)-n-1:]
        nums1 = temp
        


# ---------------- optimized solution -------------------

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i=m-1
        j=n-1
        k=len(nums1)-1
        while(j>=0):
            if i>=0 and (nums1[i]>nums2[j]):
                nums1[k]=nums1[i]
                i=i-1
            else:
                nums1[k]=nums2[j]
                j=j-1

            k=k-1

        

        