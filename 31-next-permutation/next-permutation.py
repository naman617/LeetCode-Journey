class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        if n<=1:
            return
        pivot_i=-1
        for i in range(n-2,-1,-1):
            if nums[i]<nums[i+1]:
                pivot_i=i
                break
        if pivot_i==-1:
            nums.reverse()
            return
        for j in range(n-1,pivot_i,-1):
            if nums[j]>nums[pivot_i]:
                nums[pivot_i],nums[j]=nums[j],nums[pivot_i]
                break
        left=pivot_i+1
        right=n-1
        while left<right:
            nums[left],nums[right]=nums[right],nums[left]
            left+=1
            right-=1
        