import re
class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = f"{len(strs)}|".join(strs)
        concat = ""
        for s in strs:
            concat += str(len(s))+"$"+s
        print(concat)
        return concat

    def decode(self, s: str) -> List[str]:
        res = list()
        i = 0
        while i < len(s):
            j = i
            while s[j] != "$":
                j += 1
            length = int(s[i:j])

            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j

        return res 