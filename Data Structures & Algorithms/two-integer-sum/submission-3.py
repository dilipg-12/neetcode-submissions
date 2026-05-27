class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited_nums = {}

        for i in range(len(nums)):
            reminder = target - nums[i]
            if reminder in visited_nums:
                return [visited_nums[reminder], i]
            visited_nums[nums[i]] = i