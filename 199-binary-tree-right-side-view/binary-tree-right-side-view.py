# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        q=deque([root])
        while q:
            qLen=len(q)
            rightM=None
            for i in range(qLen):
                node=q.popleft()
                if node:
                    rightM=node
                    q.append(node.left)
                    q.append(node.right)
            if rightM:
                res.append(rightM.val)
        return res


        