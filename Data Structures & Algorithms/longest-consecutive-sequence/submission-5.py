class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # if not nums:
        #     return 0
        # nums = list(set(nums))
        # nums.sort()
        # res = current = 1
        # for i in range(len(nums)):
        #     if nums[i-1] + 1 == nums[i]:
        #         current +=1
        #         res = max(res, current)
        #     else:
        #         current = 1
        # return res 
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        longest = 0
        for num in nums:
            if (num - 1) not in nums:
                length = 1
                while num + length in nums:
                    length +=1
                longest = max(longest, length)
        return longest

        