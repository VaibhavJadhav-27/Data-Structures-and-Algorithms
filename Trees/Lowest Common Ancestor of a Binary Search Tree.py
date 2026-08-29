
# ------------------------------------------------------------------------------------------------------------
# Problem no :  235
# Problem heading :  Lowest Common Ancestor of a Binary Search Tree
# Problem Link : https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/

# Problem Description : 
#   Given a binary search tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

#   The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).

#-------------------------------------------------------------------------------------------------------------

#  *******************************************************************
#   Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
#   Output: 6
#   Explanation: The LCA of nodes 2 and 8 is 6.

#   Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
#   Output: 2
#   Explanation: The LCA of nodes 2 and 4 is 2.

#  *******************************************************************
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        def dfs(node, p, q):
            if node == None:
                return None

            if node == p or node == q:
                return node
            
            left = dfs(node.left, p ,q)
            right = dfs(node.right, p ,q)

            if left and right:
                return node
            
            if left:
                return left
            
            return right
        
        return dfs(root,p,q)
        