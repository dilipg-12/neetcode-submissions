class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # nums.sort()
        # for i in range(1, len(nums)):
        #     if nums[i-1] == nums[i]:
        #         return True
        # return False
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # return len(nums) != len(set(nums))
        l = list()
        for num in nums:
            if num in l:
                return True
            l.append(num)
        return False


        