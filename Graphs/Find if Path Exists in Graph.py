
# ------------------------------------------------------------------------------------------------------------
# Problem no :  1971
# Problem heading :  Find if Path Exists in Graph
# Problem Link : https://leetcode.com/problems/find-if-path-exists-in-graph/description/

# Problem Description : 
#   There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. You are also given the integers n, source, and destination.
#   Return true if there is a valid path from source to destination, or false otherwise.

#  *******************************************************************
#   Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
#   Output: true
#   Explanation: There are two paths from source to destination: 0->1->2 and 0->2.

#   Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
#   Output: false
#   Explanation: There is no path from source to destination.
 
#  *******************************************************************
from collections import deque
class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        
        graph  = [ [] for _ in range(n)]

        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visited =  set()
        def dfs(node):
            if node == destination:
                return True
            
            if node in visited:
                return False
            
            visited.add(node)

            for neighbour in graph[node]:
                if dfs(neighbour):
                    return True
            return False
        
        return dfs(source)



