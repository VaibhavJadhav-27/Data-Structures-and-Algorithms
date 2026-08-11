
# ------------------------------------------------------------------------------------------------------------
# Problem no :  739
# Problem heading :  Daily Temperatures
# Problem Link : https://leetcode.com/problems/daily-temperatures/description/

# Problem Description : 
#   Given an array of integers temperatures representing the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. 
#   If there is no future day for which this is possible, keep answer[i] == 0 instead.


#  *******************************************************************
#   Input: temperatures = [73,74,75,71,69,72,76,73]
#   Output: [1,1,4,2,1,1,0,0]
#   Explanation:
#   For each day, we calculate the number of days to wait for a warmer temperature.

#   Input: temperatures = [30,40,50,60]
#   Output: [1,1,1,0]
#  *******************************************************************

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = []
        ans = [0] * len(temperatures)
        for nums in range(0,len(temperatures)):
            while(stack and temperatures[nums]>temperatures[stack[-1]]):
                x= stack.pop()
                ans[x] = (nums - x)

            stack.append(nums)        
            
        return ans