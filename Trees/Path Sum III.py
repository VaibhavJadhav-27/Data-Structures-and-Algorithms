
# ------------------------------------------------------------------------------------------------------------
# Problem no :  437
# Problem heading :  Path Sum III
# Problem Link : https://leetcode.com/problems/path-sum-iii/description/

# Problem Description : 
#   Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.


#-------------------------------------------------------------------------------------------------------------

#  *******************************************************************
#   Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
#   Output: 3
#   Explanation: The paths that sum to 22 are shown.

#   Input: root = [2,1,3]
#   Output: 0
#   Explanation: There are no paths in the tree with sum = 5.

#  *******************************************************************

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findPath(self, node, target):

        if node is None:
            return 0

        # subtract current node
        target -= node.val

        count = 0

        if target == 0:
            count += 1

        count += self.findPath(node.left, target)
        count += self.findPath(node.right, target)

        return count

    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: int
        """
        
        if root is None:
            return 0
        
        # path starting from current root
        count  =  self.findPath(root, targetSum)

        # Paths starting somewhere in left subtree
        count += self.pathSum(root.left, targetSum)

        # Paths starting somewhere in right subtree
        count += self.pathSum(root.right, targetSum)

        return count
    