
# ------------------------------------------------------------------------------------------------------------
# Problem no :  1797
# Problem heading :  Find Center of Star Graph
# Problem Link : https://leetcode.com/problems/find-center-of-star-graph/description/

# Problem Description : 
#   There is an undirected star graph consisting of n nodes labeled from 1 to n. 
#   A star graph is a graph where there is one center node and exactly n - 1 edges that connect the center node with every other node. 
#   You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates that there is an edge between the nodes ui and vi. 
#   Return the center of the given star graph.
#  *******************************************************************
#   Input: edges = [[1,2],[2,3],[4,2]]
#   Output: 2
#   Explanation: The center of the star graph is node 2, as it is connected to all other nodes.

#   Input: edges = [[1,2],[2,3],[3,4]]
#   Output: 2
#   Explanation: The center of the star graph is node 2, as it is connected to all other nodes.

#  *******************************************************************
class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        is_first_element_center = True
        for i in edges:
            print(i)
            if edges[0][0] in i:
                continue
            else:
                is_first_element_center =  False
                break
        if(is_first_element_center):
            return edges[0][0]
        return edges[0][1]
        