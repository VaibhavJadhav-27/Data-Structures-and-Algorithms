
# ------------------------------------------------------------------------------------------------------------
# Problem no :  94
# Problem heading :  Binary Tree Inorder Traversal
# Problem Link : https://leetcode.com/problems/binary-tree-inorder-traversal/description/

# Problem Description : 
#   Given the root of a binary tree, return the inorder traversal of its nodes' values.

#-------------------------------------------------------------------------------------------------------------

#  *******************************************************************
#   Input: root = [1,null,2,3]
#   Output: [1,3,2]

#   Input: root = []
#   Output: []

#  *******************************************************************

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) if root else []
        
