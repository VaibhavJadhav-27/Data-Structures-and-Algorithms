
# ------------------------------------------------------------------------------------------------------------
# Problem no :  1343
# Problem heading :  Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
# Problem Link : https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/description/

# Problem Description : 
#   Given an array of integers and an integer k, return the number of subarrays of size k with average greater than or equal to threshold.

#-------------------------------------------------------------------------------------------------------------

#  *******************************************************************
#   Input: arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
#   Output: 3
#   Explanation: Subarrays [2,2,2], [2,2,5], [5,5,5] have averages >= 4.

#   Input: arr = [11,13,15,17,19], k = 3, threshold = 16
#   Output: 2
#   Explanation: Subarrays [13,15,17], [17,19,11] have averages >= 16.
#  *******************************************************************
#   Explanation: The subarrays with averages >= threshold are [2,2,2], [2,2,5], [5,5,5].
#  *******************************************************************

class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        window=sum(arr[:k])
        avg = window/float(k)
        count=0
        if(avg>=threshold):
            count = count + 1
        left = 0
        for right in range(k, len(arr)):
            window = window - arr[left] + arr[right]
            avg = window/float(k)
            if(avg >= threshold):
                count = count + 1
            left = left + 1
        
        return count