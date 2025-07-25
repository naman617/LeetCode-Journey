class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh=time=0
        q=deque()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]==1:
                    fresh+=1
                if grid[r][c]==2:
                    q.append((r,c))
        directions=[[1,0],[-1,0],[0,1],[0,-1]]
        while q and fresh>0:
            for i in range(len(q)):
                r,c=q.popleft()
                for dr,dc in directions:
                    row,col=dr+r,dc+c
                    if(row in range(len(grid)) and col in range(len(grid[0])) and grid[row][col]==1):
                        grid[row][col]=0
                        fresh-=1
                        q.append((row,col))
            time+=1
        return time if fresh==0 else -1



        