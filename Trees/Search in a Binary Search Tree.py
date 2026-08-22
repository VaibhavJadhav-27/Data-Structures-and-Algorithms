
# ------------------------------------------------------------------------------------------------------------
# Problem no :  700
# Problem heading :  Search in a Binary Search Tree
# Problem Link : https://leetcode.com/problems/search-in-a-binary-search-tree/description/

# Problem Description : 
#   You are given the root of a binary search tree (BST) and an integer val.
# Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.
#-------------------------------------------------------------------------------------------------------------

#  *******************************************************************
#   Input: root = [4,2,7,1,3], val = 2
#   Output: [2,1,3]
#   Explanation: The node with value 2 is found and the subtree rooted with that node is returned.

#   Input: root = [4,2,7,1,3], val = 5
#   Output: null
#   Explanation: The node with value 5 does not exist in the tree.
#  *******************************************************************
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        
        if root is None:
            return None

        if root.val == val:
            return root

        if root.val > val:
            return self.searchBST(root.left, val)
        
        else:
            return self.searchBST(root.right, val)