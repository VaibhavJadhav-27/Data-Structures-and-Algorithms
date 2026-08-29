
# ------------------------------------------------------------------------------------------------------------
# Problem no :  105
# Problem heading :  Construct Binary Tree from Preorder and Inorder Traversal
# Problem Link : https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/

# Problem Description : 
#   Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

#-------------------------------------------------------------------------------------------------------------

#  *******************************************************************
#   Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
#   Output: [3,9,20,null,null,15,7]
#   Explanation: The binary tree is constructed from the given traversals.

#   Input: preorder = [1,2], inorder = [2,1]
#   Output: [1,2]
#   Explanation: The binary tree is constructed from the given traversals.

#  *******************************************************************
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """

        if not preorder or not inorder:
            return None

        root_val = preorder[0]

        root = TreeNode(root_val)

        mid =  inorder.index(root_val)

        root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid])

        root.right = self.buildTree(preorder[mid + 1 : ], inorder[mid + 1 :])

        return root
        