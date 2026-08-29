
# ------------------------------------------------------------------------------------------------------------
# Problem no :  56
# Problem heading :  Merge Intervals
# Problem Link : https://leetcode.com/problems/merge-intervals/description/

# Problem Description : 
#   Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.


#-------------------------------------------------------------------------------------------------------------

#  *******************************************************************
#   Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
#   Output: [[1,6],[8,10],[15,18]]
#   Explanation: Since intervals [1,3] and [2,6] overlap, they are merged into [1,6].

#   Input: intervals = [[1,4],[4,5]]
#   Output: [[1,5]]
#   Explanation: Intervals [1,4] and [4,5] are considered overlapping.

#  *******************************************************************

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        
        intervals.sort(key=lambda x:x[0])

        result = [intervals[0]]

        for current in intervals[1:]:
            last = result[-1]

            if current[0] <= last[1]:
                if current[1] > last[1]:
                    ans = result.pop()
                    result.append([last[0],current[1]])
            else:
                result.append(current)
        return result