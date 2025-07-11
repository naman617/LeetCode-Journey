class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS,COLS=len(image),len(image[0])
        oc=image[sr][sc]
        if oc==color:
            return image
        def dfs(r,c):
            if not (0<=r<ROWS and 0<=c<COLS and image[r][c]==oc):
                return
            image[r][c]=color
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        
        dfs(sr,sc)
        return image
        