
# ------------------------------------------------------------------------------------------------------------
# Problem no :  1523
# Problem heading :  Count Odd Numbers in an Interval Range
# Problem Link : https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/description/?envType=daily-question&envId=2025-12-07 

# Problem Description : 
#   Given two non-negative integers low and high. 
#   Return the count of odd numbers between low and high (inclusive).

#-------------------------------------------------------------------------------------------------------------

#  *******************************************************************
#   Input: low = 3, high = 7
#   Output: 3
#   Explanation: The odd numbers between 3 and 7 are [3,5,7].

#   Input: low = 8, high = 10
#   Output: 1
#   Explanation: The odd numbers between 8 and 10 are [9].
#  *******************************************************************


class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        odd_count = 0
        start_point= 0
        endpoint = 0
        if((low%2)!=0):
            start_point=low
        else:
            start_point=low+1
        if((high%2)!=0):
            endpoint=high
        else:
            endpoint = high - 1
        odd_count = (endpoint - start_point)//2 + 1
        return odd_count

        # Approach 2
        # return (high + 1) // 2 - low // 2   