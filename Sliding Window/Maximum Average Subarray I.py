
# ------------------------------------------------------------------------------------------------------------
# Problem no :  643
# Problem heading :  Maximum Average Subarray I
# Problem Link : https://leetcode.com/problems/maximum-average-subarray-i/description/

# Problem Description : 
#   Given an array of integers and a window size k, find the maximum average of all subarrays of size k.
#   Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

 

#-------------------------------------------------------------------------------------------------------------

#  *******************************************************************
#   Input: nums = [1,12,-5,-6,50,3], k = 4
#   Output: 12.75000

#   Input: nums = [5], k = 1
#   Output: 5.00000
#  *******************************************************************

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        window_sum = 0
        for i in range(k):
            window_sum =  window_sum + nums[i]

        max_avg = window_sum / float(k)
        start=0
        end=k
        while ( end < len(nums)):
            window_sum =  window_sum - nums[start]
            window_sum =  window_sum + nums[end]
            start = start+1
            end = end + 1 

            max_avg = max(window_sum / float(k),max_avg)
        return max_avg

        