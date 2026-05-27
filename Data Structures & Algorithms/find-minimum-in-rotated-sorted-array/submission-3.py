class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        s = float("inf")
        while l<=r:
            m = (l+r)//2
            if nums[m] > nums[r]:
                l = m + 1
            elif nums[m] <= nums[r]:
                s = min(s, nums[m])
                r = m - 1
        return -1 if s== float("inf") else s
        