class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = {}
        l = 0

        for r, char in enumerate(s):
            d[char] = d.get(char, 0) + 1
            if (r - l + 1) - max(d.values()) > k:
                d[s[l]] -= 1
                l += 1
        return len(s) - l
        