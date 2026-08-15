
# ------------------------------------------------------------------------------------------------------------
# Problem no :  144
# Problem heading :  Binary Tree Preorder Traversal
# Problem Link : https://leetcode.com/problems/binary-tree-preorder-traversal/description/

# Problem Description : 
#   Given the root of a binary tree, return the preorder traversal of its nodes' values.

#-------------------------------------------------------------------------------------------------------------

#  *******************************************************************
#   Input: root = [1,null,2,3]
#   Output: [1,2,3]

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
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        ret = []
        stack = [root]

        while stack:
            node = stack.pop()
            if(node):
                ret.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return ret
    
    
# ---------------------- Recursive Solution ----------------------
  
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """

        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right) if root else []