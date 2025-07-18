# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root==p or root==q:
            return root
        left_lca=self.lowestCommonAncestor(root.left,p,q)
        right_lca=self.lowestCommonAncestor(root.right,p,q)
        if left_lca and right_lca:
            return root
        return left_lca or right_lca
        