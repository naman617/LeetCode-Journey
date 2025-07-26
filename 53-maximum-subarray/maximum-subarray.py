class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub,preSum=nums[0],0
        for num in nums:
            if preSum<0:
                preSum=0
            preSum+=num
            maxSub=max(maxSub,preSum)
        return maxSub