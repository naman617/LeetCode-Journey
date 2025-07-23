class Solution:
    def calculate(self, s: str) -> int:
        num=0
        total=0
        sign=1
        stack=[]
        for char in s:
            if char.isdigit():
                num=(num*10)+int(char)
            elif char in "+-":
                total+=num*sign
                num=0
                sign=1 if char =='+' else -1
            elif char=='(':
                stack.append(total)
                stack.append(sign)
                total=0
                sign=1
            elif char==')':
                total+=num*sign
                prev_sign=stack.pop()
                prev_total=stack.pop()
                total=prev_total+(prev_sign*total)
                num=0
                sign=1
        total+=num*sign
        return total

        