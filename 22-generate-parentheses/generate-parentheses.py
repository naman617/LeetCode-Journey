class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        stack=[]
        def pa(openN,closedN):
            if openN==closedN==n:
                res.append("".join(stack))
                return
            if openN<n:
                stack.append('(')
                pa(openN+1,closedN)
                stack.pop()
            if closedN<openN:
                stack.append(')')
                pa(openN,closedN+1)
                stack.pop()
        pa(0,0)
        return res
        