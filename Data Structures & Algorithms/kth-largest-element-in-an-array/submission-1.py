class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # nums.sort(reverse=True)
        # print(nums)
        # return nums[k-1]
        # ~~~~~~~~~~~~~~~~~~~~~~
        nums = [-n for n in nums]
        heapq.heapify(nums)
        while k > 1:
            heapq.heappop(nums)
            k-=1
        return -heapq.heappop(nums)
