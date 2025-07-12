# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q=deque([root])
        res=[]
        ltr=True
        while q:
            qLen=len(q)
            curr_level=[]
            for i in range(qLen):
                node=q.popleft()
                curr_level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if not ltr:
                curr_level.reverse()
            res.append(curr_level)
            ltr=not ltr
        return res
        