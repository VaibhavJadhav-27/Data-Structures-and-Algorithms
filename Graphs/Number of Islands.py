
# ------------------------------------------------------------------------------------------------------------
# Problem no :  200
# Problem heading :  Number of Islands
# Problem Link : https://leetcode.com/problems/number-of-islands/description/

# Problem Description : 
#   Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
#   An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

#  *******************************************************************
#   Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
#  ]
#   Output: 4
#   Explanation: There are 4 islands in the grid.

#   Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
#  ]
#   Output: 3
#   Explanation: There are 3 islands in the grid.
 
#  *******************************************************************

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])

        count_of_islands = 0
        def dfs(r, c):
            if r < 0 or c < 0 or r >=rows or c >= cols:
                return
            
            # only process 1:
            if grid[r][c] != "1":
                return
            
            #turn land into water
            grid[r][c] = "0"

            #explore directions
            for dr,dc in [(-1,0), (0,1), (1,0), (0,-1)]:
                dfs(r + dr, c+ dc)

        count = 0
        for r in range(0,rows):
            for c in range(0,cols):
                if grid[r][c] == "1":
                    count = count + 1
                    dfs(r,c)

        return count