# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, arr):
        if not root:
            return
        self.dfs(root.left, arr)
        arr.append(root.val)
        self.dfs(root.right, arr)
        
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        arr = []
        self.dfs(root, arr)
        minn = arr[1] - arr[0]
        n = len(arr)
        for i in range(n - 1, 0, -1):
            minn = min(minn, arr[i] - arr[i - 1])
        return minn