class Solution:
    def calculate(self, s: str) -> int:
        num=0
        sign='+'
        stack=[]
        for i,char in enumerate(s):
            if char.isdigit():
                num=(num*10)+int(char)
            if char in '+-*/' or i==len(s)-1:
                if sign=='+':
                    stack.append(num)
                elif sign=='-':
                    stack.append(-num)
                elif sign=='*':
                    stack[-1]=stack[-1]*num
                if sign=='/':
                    stack[-1]=int(stack[-1]/num)
                sign=char
                num=0
        return sum(stack)       