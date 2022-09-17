# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if self.heightTree(root) == -1 :
            return False
        else:
            return True
        
    def heightTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        # Height of left subtree
        leftHeight = self.heightTree(root.left)
        if leftHeight == -1:
            return -1
        
        # Height of left subtree
        rightHeight = self.heightTree(root.right)
        if rightHeight == -1:
            return -1
        
        if (abs(leftHeight - rightHeight) > 1):
            return -1
        else:
            return max(leftHeight, rightHeight) + 1