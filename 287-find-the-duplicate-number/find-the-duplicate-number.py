class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hse=set()
        for i in nums:
            if i in hse:
                return i
            hse.add(i)