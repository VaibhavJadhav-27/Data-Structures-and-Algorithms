
# ------------------------------------------------------------------------------------------------------------
# Problem no :  547
# Problem heading :  Number of Provinces
# Problem Link : https://leetcode.com/problems/number-of-provinces/description/

# Problem Description : 
#   There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.
#   A province is a group of directly or indirectly connected cities and no other cities outside of the group.
#   You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.
#   Return the total number of provinces.

#  *******************************************************************
#   Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
#   Output: 2
#   Explanation: The cities are grouped into two provinces: {0,1} and {2}.

#   Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
#   Output: 3
#   Explanation: Each city is its own province.

#  *******************************************************************
class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        n = len(isConnected)
        visited = set()
        count  = 0

        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)

            for neighbour in range(n):
                if isConnected[node][neighbour] == 1:
                    dfs(neighbour)

        for i in range(n):
            if i not in visited:
                count =  count + 1
                dfs(i)

        return count
        