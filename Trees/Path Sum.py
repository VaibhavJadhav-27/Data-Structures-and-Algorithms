
# ------------------------------------------------------------------------------------------------------------
# Problem no :  112
# Problem heading :  Path Sum
# Problem Link : https://leetcode.com/problems/path-sum/description/

# Problem Description : 
#   Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.


#-------------------------------------------------------------------------------------------------------------

#  *******************************************************************
#   Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
#   Output: True
#   Explanation: The root-to-leaf path with the target sum is shown.

#   Input: root = [2,1,3]
#   Output: False
#   Explanation: There two root-to-leaf paths in the tree:
#   (2 -> 1): The sum is 2 + 1 = 3
#   (2 -> 3): The sum is 2 + 3 = 5
#   There is no root-to-leaf path with sum = 5.

#  *******************************************************************
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        if root is None:
            return False
        
        stack = []
        curr_sum = root.val
        stack.append((root,curr_sum))
        while stack:
            node, curr_sum = stack.pop()

            if(node.left is None and node.right is None):
                if curr_sum==targetSum:
                    return True
                continue

            if node.right:
                stack.append((node.right, curr_sum + node.right.val))
            if node.left:
                stack.append((node.left, curr_sum + node.left.val))
        return False
