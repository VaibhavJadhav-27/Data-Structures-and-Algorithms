
# ------------------------------------------------------------------------------------------------------------
# Problem no :  226
# Problem heading :  Invert Binary Tree
# Problem Link : https://leetcode.com/problems/invert-binary-tree/description/

# Problem Description : 
#   Given the root of a binary tree, invert the tree, and return its root.

#-------------------------------------------------------------------------------------------------------------

#  *******************************************************************
#   Input: root = [4,2,7,1,3,6,9]
#   Output: [4,7,2,9,6,3,1]

#   Input: root = [2,1,3]
#   Output: [2,3,1]

#  *******************************************************************
from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        
        if root is None:
            return
        queue =  deque()
        queue.append(root)

        while queue:
            node = queue.popleft()

            node.left , node.right =  node.right, node.left
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root


#------------------------- Recursive Solution ------------------------- ##

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """

        if root is None:
            return None
        
        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root