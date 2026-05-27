class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # ans = [1] * len(nums)
        # for i in range(len(nums)):
        #     product = 1
        #     for j in range(len(nums)):
        #         if i == j:
        #             continue
        #         product *= nums[j]
        #     ans[i] = product
        # return ans
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        n = len(nums)
        ans = [1] * n
        prefi = 1
        sufi = 1
        for i in range(n):
            ans[i] = prefi
            prefi *= nums[i]
        for i in range(n-1,-1,-1):
            ans[i] *= sufi
            sufi *= nums[i]
        return ans


