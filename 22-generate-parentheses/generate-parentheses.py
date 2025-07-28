class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack=[]
        res=[]
        def gp(openN,closedN):
            if openN==closedN==n:
                res.append("".join(stack))
                return
            if openN<n:
                stack.append('(')
                gp(openN+1,closedN)
                stack.pop()
            if closedN<openN:
                stack.append(')')
                gp(openN,closedN+1)
                stack.pop()
        gp(0,0)
        return res
        