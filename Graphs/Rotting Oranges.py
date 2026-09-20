
# ------------------------------------------------------------------------------------------------------------
# Problem no : 994
# Problem heading :  Rotting Oranges
# Problem Link : https://leetcode.com/problems/rotting oranges/description/

# Problem Description : 
#   You are given an m x n grid where each cell can have one of three values:
#   0 representing an empty cell,
#   1 representing a fresh orange, or
#   2 representing a rotten orange.
#   Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

#   Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

#  *******************************************************************
#   Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
#   Output: 4

#   Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
#   Output: -1
#   Explanation: There is no way to rot all fresh oranges.

#   Input: grid = [[0,2]]
#   Output: 0
#   Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.

#  *******************************************************************
from collections import deque
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        fresh = 0

        directions = [(0,-1),(0,1),(1,0),(-1,0)]
        for r in range(0,rows):
            for c in range(0,cols):
                if grid[r][c] == 2:
                    queue.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1
        minutes = 0
        while queue and fresh > 0:

            for _ in range(len(queue)):
                row,col = queue.popleft()

                for dr, dc in directions:
                    nr = row + dr
                    nc = col + dc

                    if nc<0 or nr<0 or nr>=rows or nc>=cols:
                        continue
                    
                    if grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh = fresh - 1
                        queue.append((nr,nc))
            minutes = minutes + 1
        

        if fresh > 0:
            return -1
        return minutes


