# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not root:
            return []
        graph=defaultdict(list)
        q=deque([root])
        while q:
            node=q.popleft()
            if node.left:
                graph[node].append(node.left)
                graph[node.left].append(node)
                q.append(node.left)
            if node.right:
                graph[node].append(node.right)
                graph[node.right].append(node)
                q.append(node.right)
        qu=deque([(target,0)])
        visited={target}
        res=[]
        while qu:
            node,dist=qu.popleft()
            if dist==k:
                res.append(node.val)
            if dist<k:
                for neighbour in graph[node]:
                    if neighbour not in visited:
                        visited.add(neighbour)
                        qu.append((neighbour,dist+1))
        return res


            
        