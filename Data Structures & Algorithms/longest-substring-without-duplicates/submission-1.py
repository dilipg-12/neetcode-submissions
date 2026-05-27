class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {} # char -> index
        left = 0
        res = 0
        for right, char in enumerate(s):
            if char in char_map and char_map[char] >= left:
                left = char_map[char] + 1
            
            res = max(res, right - left + 1)
            char_map[char] = right # Update to the latest index
            
        return res
        