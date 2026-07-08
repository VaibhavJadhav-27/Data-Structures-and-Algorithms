
# ------------------------------------------------------------------------------------------------------------
# Problem no :  11
# Problem heading :  Container With Most Water
# Problem Link : https://leetcode.com/problems/container-with-most-water/description/

# Problem Description : 
#   You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
#   Find two lines that together with the x-axis form a container, such that the container contains the most water.
#   Return the maximum amount of water a container can store.

#-------------------------------------------------------------------------------------------------------------

#  *******************************************************************
#   Input: height = [1,8,6,2,5,4,8,3,7]
#   Output: 49
#
#   Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
#   Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
#
#  *******************************************************************

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i=0
        j=len(height)-1
        max_amount=0
        while(i<j):
            dist=j-i
            min_val=min(height[i],height[j])
            area=dist*min_val
            if(area>max_amount):
                max_amount=area
            if(height[i]>height[j]):
                j=j-1
            else:
                i=i+1
        return max_amount