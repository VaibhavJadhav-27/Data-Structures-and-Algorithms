
# ------------------------------------------------------------------------------------------------------------
# Problem no :  104
# Problem heading :  Maximum Depth of Binary Tree
# Problem Link : https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

# Problem Description : 
#   Given the root of a binary tree, return its maximum depth.

#-------------------------------------------------------------------------------------------------------------

#  *******************************************************************
#   Input: root = [3,9,20,null,null,15,7]
#   Output: 3

#   Input: [1,null,2]
#   Output: 2

#  *******************************************************************

from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root is None:
            return 0
        queue  =  deque([root])
        depth = 0

        while queue:
            level_size = len(queue)
            depth = depth + 1
            for _ in range(level_size):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return depth
    
    
## ------------------------- Recursive Solution ------------------------- ##

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):

        if root is None:
            return 0
        
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return 1+max(left, right)