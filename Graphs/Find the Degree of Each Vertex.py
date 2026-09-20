
# ------------------------------------------------------------------------------------------------------------
# Problem no :  3898
# Problem heading :  Find the Degree of Each Vertex
# Problem Link : https://leetcode.com/problems/find-the-degree-of-each-vertex/description/

# Problem Description : 
#   You are given an integer n and a 2D integer array edges of length n - 1, where edges[i] = [ui, vi] represents an undirected edge between vertices ui and vi. Return the degree of each vertex.

#  *******************************************************************
#   Input: matrix = [[0,1,1],[1,0,1],[1,1,0]]
#   Output: [2,2,2]
#   Explanation: The degree of each vertex is as follows:
#   - Vertex 0: 2
#   - Vertex 1: 2
#   - Vertex 2: 2

#   Input: matrix = [[0,1,0],[1,0,0],[0,0,0]]
#   Output: [1,2,1]
#   Explanation: The degree of each vertex is as follows:
#   - Vertex 0: 1
#   - Vertex 1: 2
#   - Vertex 2: 1
 
#  *******************************************************************
class Solution(object):
    def findDegrees(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ans=[]
        for i in matrix:
            ans.append(sum(i))
        return ans