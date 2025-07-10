class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        unique_nums=set(nums)
        if 0 in unique_nums:
            unique_nums.remove(0)
        return len(unique_nums)
        