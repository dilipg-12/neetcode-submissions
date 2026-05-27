class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ll = list()
        l = 0
        for r in range(k, len(nums) +1):
            ll.append(max(nums[l:r]))
            l += 1
        return ll
        