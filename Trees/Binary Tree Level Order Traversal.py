
# ------------------------------------------------------------------------------------------------------------
# Problem no :  102
# Problem heading :  Binary Tree Level Order Traversal
# Problem Link : https://leetcode.com/problems/binary-tree-level-order-traversal/description/

# Problem Description : 
#   Given the root of a binary tree, return the level order traversal of its nodes' values.

#-------------------------------------------------------------------------------------------------------------

#  *******************************************************************
#   Input: root = [3,9,20,null,null,15,7]
#   Output: [[3],[9,20],[15,7]]

#   Input: root = []
#   Output: []

#  *******************************************************************

from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        ans = []
        queue  =  deque([root])

        while queue:
            level_size = len(queue)
            temp = []

            for _ in range(level_size):
                node = queue.popleft()

                temp.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(temp)
        return ans
            