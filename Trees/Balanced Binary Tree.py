
# ------------------------------------------------------------------------------------------------------------
# Problem no :  110
# Problem heading :  Balanced Binary Tree
# Problem Link : https://leetcode.com/problems/balanced-binary-tree/description/

# Problem Description : 
#   Given the root of a binary tree, return true if it is a height-balanced binary tree.
#   A height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differs by more than one.

#-------------------------------------------------------------------------------------------------------------

#  *******************************************************************
#   Input: root = [3,9,20,null,null,15,7]
#   Output: True
#   Explanation: The tree is height-balanced.

#   Input: root = [1,2,2,3,3,null,null,4,4]
#   Output: False
#   Explanation: The tree is not height-balanced.
#  *******************************************************************
# Definition for a binary tree node.
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        def dfs(node):
            if node is None:
                return 0
            
            left_height = dfs(node.left)
            if left_height == -1:
                return -1
            
            right_height = dfs(node.right)
            if right_height == -1:
                return -1

            diff = abs(left_height - right_height)
            if diff > 1:
                return  -1
            return 1+max(left_height, right_height)
            
        
        temp = dfs(root)
        if(temp== -1):
            return False
        else:
            return True
        