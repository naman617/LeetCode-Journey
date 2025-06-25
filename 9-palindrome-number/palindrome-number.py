class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0 or (x%10==0 and x!=0):
            return False
        rev_num=0
        while rev_num<x:
            l_d=x%10
            rev_num=(rev_num*10)+l_d
            x=x//10
        return x==rev_num or x==rev_num//10        