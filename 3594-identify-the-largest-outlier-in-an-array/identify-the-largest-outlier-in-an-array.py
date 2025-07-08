class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        counts=Counter(nums)
        total_sum=sum(nums)
        outlier=float('-inf')
        for num in nums:
            counts[num]-=1
            total_sum-=num
            if total_sum%2==0 and counts[total_sum//2]>0:
                outlier=max(outlier,num)
            counts[num]+=1
            total_sum+=num
        return outlier

        