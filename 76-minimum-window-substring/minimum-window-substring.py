class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

    
        t_counts = collections.Counter(t)

    
        left = 0
        required = len(t_counts)
        formed = 0

        window_counts = {}

    
        ans = (float('inf'), None, None)

    
        for right, char in enumerate(s):
        
            window_counts[char] = window_counts.get(char, 0) + 1

        
            if char in t_counts and window_counts[char] == t_counts[char]:
                formed += 1
        
        
            while left <= right and formed == required:
            
                if (right - left + 1) < ans[0]:
                    ans = (right - left + 1, left, right)

            
                left_char = s[left]

            
                window_counts[left_char] -= 1

            
                if left_char in t_counts and window_counts[left_char] < t_counts[left_char]:
                    formed -= 1

           
                left += 1

   
        return "" if ans[0] == float('inf') else s[ans[1] : ans[2] + 1]