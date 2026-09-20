
# ------------------------------------------------------------------------------------------------------------
# Problem no :  733
# Problem heading :  Flood Fill
# Problem Link : https://leetcode.com/problems/flood-fill/description/

# Problem Description : 
#   An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.
#   You are also given three integers sr, sc, and newColor. You should perform a flood fill on the image starting from the pixel image[sr][sc].
#   To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with newColor.
#   Return the modified image after performing the flood fill.

#  *******************************************************************
#   Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2
#   Output: [[2,2,2],[2,2,0],[2,0,1]]
#   Explanation: From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected by a path of the same color as the starting pixel are colored with the new color.
#   Note the bottom pixel (with position (2, 1)) is not colored because it is not 4-directionally connected to the starting pixel.

#   Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, newColor = 0
#   Output: [[0,0,0],[0,0,0]]
#   Explanation: The starting pixel is already colored with the target color.


#  *******************************************************************
from collections import deque
class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        old_color = image[sr][sc]

        if old_color == color:
            return image
        
        rows = len(image)
        cols = len(image[0])

        def dfs(r,c):
            # check boundaries:
            if r < 0 or c < 0 or r >=rows or c >= cols:
                return 
            
            # only process original color:
            if image[r][c] != old_color:
                return
            
            # change current color
            image[r][c] = color

            # explore directions
            for dr,dc in [(-1,0), (0,1), (1,0), (0,-1)]:
                dfs(r + dr, c+ dc)
        
        dfs(sr,sc)

        return image

