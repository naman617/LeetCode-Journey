class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        l=0
        res=total=0
        for r in range(len(nums)):
            total+=nums[r]
            while (r-l+1)*nums[r]>total+k:
                total-=nums[l]
                l+=1
            res=max(res,(r-l+1))
        return res
