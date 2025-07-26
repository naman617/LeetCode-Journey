class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        closeToOpen={')':'(',']':'[','}':'{'}
        for c in range(len(s)):
            if s[c] in closeToOpen:
                if stack and stack[-1]==closeToOpen[s[c]]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[c])
        return True if not stack else False
        