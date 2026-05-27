class Solution:
    def isValid(self, s: str) -> bool:
        valid_bucket = {'}': '{', ')': '(', ']':'['}
        ll = list()
        for c in s:
            if c in valid_bucket:
                if ll and ll[-1] == valid_bucket[c]:
                    ll.pop()
                else:
                    return False
            else:
                ll.append(c)
        return not ll
        