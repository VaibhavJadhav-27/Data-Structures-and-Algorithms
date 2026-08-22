
# ------------------------------------------------------------------------------------------------------------
# Problem no :  543
# Problem heading :  Diameter of Binary Tree
# Problem Link : https://leetcode.com/problems/diameter-of-binary-tree/description/

# Problem Description : 
#   Given the root of a binary tree, return the length of the diameter of the tree.
#   The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

#-------------------------------------------------------------------------------------------------------------

#  *******************************************************************
#   Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1]
#   Output: 4
#   Explanation: The diameter is 4, which is the length of the path [11,4,8,13] or [7,2,8,13].

#   Input: root = [2,1,3]
#   Output: 2
#   Explanation: The diameter is 2, which is the length of the path [1,2,3].
#  *******************************************************************
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        
        diameter = [0]

        def dfs(node):
            if node is None:
                return 0

            left_height = dfs(node.left)
            right_height = dfs(node.right)

            diameter[0] = max(diameter[0], left_height + right_height)
            return 1 + max(left_height,right_height)

        dfs(root)

        return diameter[0]