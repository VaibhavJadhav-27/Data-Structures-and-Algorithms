
# ------------------------------------------------------------------------------------------------------------
# Problem no :  695
# Problem heading :  Max Area of Island
# Problem Link : https://leetcode.com/problems/max-area-of-island/description/

# Problem Description : 
#   You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
#   The area of an island is the number of cells with a value 1 in the island.
#   Return the maximum area of an island in grid. If there is no island, return 0.

#  *******************************************************************
#   Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
#   Output: 6
#   Explanation: The answer is not 11, because the island must be connected 4-directionally.

#   Input: grid = [[0,0,0,0,0,0,0,0]]
#   Output: 0
#   Explanation: There is no island.

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
        