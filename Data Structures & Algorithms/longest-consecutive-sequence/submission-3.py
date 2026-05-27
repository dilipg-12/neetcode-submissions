class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
            if not nums:
                return 0
            nums = list(set(nums))
            nums.sort()
            res = current = 1
            for i in range(len(nums)):
                if nums[i-1] + 1 == nums[i]:
                    current +=1
                    res = max(res, current)
                else:
                    current = 1
            return res 
        