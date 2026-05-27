class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        s1_count = [0] * 26
        s2_count = [0] * 26

        for i in range(len(s1)):
            s1_count[ord(s1[i]) -97] += 1
            s2_count[ord(s2[i]) -97] += 1

        if s1_count == s2_count:
            return True

        for j in range(len(s1), len(s2)):
            s2_count[ord(s2[j]) -97] +=1

            s2_count[ord(s2[j - len(s1)]) -97] -=1

            if s1_count == s2_count:
                return True

        return False


        