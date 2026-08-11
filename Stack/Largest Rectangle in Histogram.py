
# ------------------------------------------------------------------------------------------------------------
# Problem no :  84
# Problem heading :  Largest Rectangle in Histogram
# Problem Link : https://leetcode.com/problems/largest-rectangle-in-histogram/description/

# Problem Description : 
#   Given an array of integers heights representing the histogram's bar height where the width of each bar is 1,
#   return the area of the largest rectangle in the histogram.

#  *******************************************************************
#   Input: heights = [2,1,5,6,2,3]
#   Output: 10
#   Explanation:
#   The largest rectangle is shown in the above histogram where the area is 10.

#   Input: heights = [2,4]
#   Output: 4

#  *******************************************************************

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        max_area = 0
        stack = []

        for i in range(len(heights) + 1):

            if i == len(heights):
                current_height = 0
            else:
                current_height = heights[i]

            while stack and current_height < heights[stack[-1]]:

                x = stack.pop()
                height = heights[x]

                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i

                area = height * width
                max_area = max(max_area, area)

            if i < len(heights):
                stack.append(i)

        return max_area