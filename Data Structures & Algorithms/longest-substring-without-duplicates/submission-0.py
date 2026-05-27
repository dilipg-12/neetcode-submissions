class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char = dict()
        res = l = 0
        for i,r in enumerate(s):
            if r in char and char[r] >= l:
                l = char[r] + 1
            res = max(res, i - l + 1)
            char[r] = i
        return res
        