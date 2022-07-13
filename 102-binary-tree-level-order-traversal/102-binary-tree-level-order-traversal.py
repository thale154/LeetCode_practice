# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        ans, level = [], [root]
        while level:
            ans.append([node.val for node in level])
            level = [nextLeaf for next in level for nextLeaf in (next.left, next.right) if nextLeaf]
        return ans