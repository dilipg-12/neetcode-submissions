class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): return ""
        t_count = dict()
        window = dict()
        for char in t:
            t_count[char] = t_count.get(char,0) + 1
            window[char] = 0

        l = 0
        ans = float("inf"), 0, 0
        need, have = len(t_count), 0

        for r, char in enumerate(s):
            if char in t_count:
                window[char] += 1
                if window[char] == t_count[char]:
                    have += 1

            while have == need:
                if (r - l + 1) < ans[0]:
                    ans = (r - l + 1), l, r
                left_char = s[l]
                if left_char in window:
                    window[left_char] -= 1
                    if window[left_char] < t_count[left_char]:
                        have -= 1
                l+=1

        return s[ans[1]: ans[2] +1] if ans[0] != float("inf") else ""
            


        