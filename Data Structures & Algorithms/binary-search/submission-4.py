class Solution:
    def search(self, nums: List[int], target: int) -> int:
        r = len(nums) - 1
        l = 0
        while l <= r:
            f =  l + (r - l) // 2
            f = (l+r)//2
            mid = nums[f]
            if mid < target:
                l = f + 1
            elif mid > target:
                r = f - 1
            else:
                return f
        return -1
        