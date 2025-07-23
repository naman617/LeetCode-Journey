class Solution:
    def calculate(self, s: str) -> int:
        nums=0
        sign='+'
        stack=[]
        for i,char in enumerate(s):
            if char.isdigit():
                nums=(nums*10)+int(char)
            if char in "+-*/" or i==len(s)-1:
                if sign=='+':
                    stack.append(nums)
                elif sign=='-':
                    stack.append(-nums)
                elif sign=='*':
                    stack[-1]=stack[-1]*nums
                elif sign=='/':
                    stack[-1]=int(stack[-1]/nums)
                sign=char
                nums=0
        return sum(stack)

        