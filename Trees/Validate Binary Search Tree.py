
# ------------------------------------------------------------------------------------------------------------
# Problem no :  98
# Problem heading :  Validate Binary Search Tree
# Problem Link : https://leetcode.com/problems/validate-binary-search-tree/description/

# Problem Description : 
#   You are given the root of a binary tree, determine if it is a valid binary search tree (BST).
#   A valid BST is defined as follows:
#   The left subtree of a node contains only nodes with keys strictly less than the node's key.
#   The right subtree of a node contains only nodes with keys strictly greater than the node's key.
#   Both the left and right subtrees must also be binary search trees.
#-------------------------------------------------------------------------------------------------------------

#  *******************************************************************
#   Input: root = [2,1,3]
#   Output: True
#   Explanation: The tree is a valid BST.

#   Input: root = [5,1,4,null,null,3,6]
#   Output: False
#   Explanation: The root node's value is 5 but its right child's value is 4.
#  *******************************************************************

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        
        if root is None:
            return None

        def dfs(node):
            if node is None:
                return (True, float('inf'),float('-inf'))
            
            left_valid , left_min, left_max = dfs(node.left)
            right_valid, right_min, right_max = dfs(node.right)

            if not left_valid or not right_valid:
                return (False,0 ,0)
            
            if(node.val <= left_max or node.val >= right_min):
                return (False,0 ,0)
            
            minimum = min(node.val, left_min, right_min)
            maximum = max(node.val, right_max, left_max)

            return (True, minimum, maximum)

        valid, _, _ = dfs(root)
        return valid