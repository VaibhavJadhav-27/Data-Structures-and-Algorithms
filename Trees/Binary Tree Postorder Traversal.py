
# ------------------------------------------------------------------------------------------------------------
# Problem no :  145
# Problem heading :  Binary Tree Postorder Traversal
# Problem Link : https://leetcode.com/problems/binary-tree-postorder-traversal/description/

# Problem Description : 
#   Given the root of a binary tree, return the postorder traversal of its nodes' values.

#-------------------------------------------------------------------------------------------------------------

#  *******************************************************************
#   Input: root = [1,null,2,3]
#   Output: [3,2,1]

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
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """

        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val] if root else []