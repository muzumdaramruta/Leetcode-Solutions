# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        targets = {p, q}
        def dfs(node):
            if not node or node in targets:
                return node
            L = dfs(node.left)
            R = dfs(node.right)
            if L and R:
                return node
            return L or R

        return dfs(root)