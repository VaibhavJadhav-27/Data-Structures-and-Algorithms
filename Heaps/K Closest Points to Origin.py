# ------------------------------------------------------------------------------------------------------------
# Problem no :  973
# Problem heading :  K Closest Points to Origin
# Problem Link : https://leetcode.com/problems/k-closest-points-to-origin/description/

# Problem Description :
#   The input is a list of points represented by their x- and y-coordinates, along with k, the number of points to select.
#   Select the points nearest to the origin (0, 0).
#   Closeness is measured by Euclidean distance.
#   The selected points may be returned in any order, and the selected set is unique.

#-------------------------------------------------------------------------------------------------------------

#  *******************************************************************
#   Input: points = [[1,3],[-2,2]], k = 1
#   Output: [[-2,2]]
#   Explanation: The point [-2,2] is closer to the origin than [1,3].
#  *******************************************************************

#   Input: points = [[3,3],[5,-1],[-2,4]], k = 2
#   Output: [[3,3],[-2,4]]
#   Explanation: These are the two closest points; their order may be swapped.

#  *******************************************************************

import heapq
import math
class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        
        heap = []
        for x,y in points:
            distance = math.sqrt(((0-x)**2) + ((0-y)**2))
            heapq.heappush(heap,(distance,[x,y]))
        ans= []
        for i in range(0,k):
            closest,temp = heapq.heappop(heap)
            ans.append(temp)
        return ans
