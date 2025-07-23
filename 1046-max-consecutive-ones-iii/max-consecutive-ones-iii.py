class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l=0
        no_of_zero=0
        max_len=0
        for r in range(len(nums)):
            if nums[r]==0:
                no_of_zero+=1
            while no_of_zero>k:
                if nums[l]==0:
                    no_of_zero-=1
                l+=1
            cur_len=r-l+1
            max_len=max(max_len,cur_len)
        return max_len

        