# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.targetSum = targetSum
        self.res = []
        self.helpFunction(root, 0, [])
        return self.res
        
    def helpFunction(self, node: Optional[TreeNode], currentSum: int, curPath: List[int]) -> List[List[int]]:
        if not node:
            return None
        currentSum += node.val
        curPath.append(node.val)
        if (not node.left) and (not node.right):
            if (currentSum == self.targetSum):
                self.res.append(curPath.copy())
        else:
            self.helpFunction(node.left, currentSum, curPath)
            self.helpFunction(node.right, currentSum, curPath)
        curPath.pop()
        