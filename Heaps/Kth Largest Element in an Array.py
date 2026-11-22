
# ------------------------------------------------------------------------------------------------------------
# Problem no :  215
# Problem heading :  Kth Largest Element in an Array
# Problem Link : https://leetcode.com/problems/kth-largest-element-in-an-array/description/?envType=problem-list-v2&envId=dm218mbe

# Problem Description : 
#   Given an integer array nums and an integer k, return the kth largest element in the array.
#   Note that it is the kth largest element in the sorted order, not the kth distinct element.
#   Can you solve it without sorting?

#-------------------------------------------------------------------------------------------------------------

#  *******************************************************************
#   Input: nums = [3,2,1,5,6,4], k = 2
#   Output: 5
#  *******************************************************************

#   Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
#   Output: 4

#  *******************************************************************

import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        heap = []
        for i in nums:
            heapq.heappush(heap,-i)

        x=1
        while(x<k):
            heapq.heappop(heap)
            x=x+1
        if heap:
            return -heapq.heappop(heap)
