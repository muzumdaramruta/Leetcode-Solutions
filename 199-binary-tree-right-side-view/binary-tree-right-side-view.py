# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        if not root:
            return []

        q = collections.deque()
        q.append(root)
        lastNode = None

        while q:
            qLen = len(q)
            
            for i in range(qLen):
                node = q.popleft()
                if node:
                    q.append(node.left) if node.left else None
                    q.append(node.right) if node.right else None
                    lastNode = node
                    
            res.append(lastNode.val)
        return res