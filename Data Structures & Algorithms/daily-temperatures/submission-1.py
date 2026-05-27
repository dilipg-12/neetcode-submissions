class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = list()
        l = r = 0
        while l <= len(temperatures) -1:
            r +=  1
            if r == len(temperatures):
                res.append(0)
                l += 1
                r = l
            elif temperatures[r] > temperatures[l]:
                res.append(r - l)
                l += 1
                r = l
        return res
        while l <= len(temperatures) -1:
            if temperatures[r] > temperatures[l]:
                res.append(r - l)
                l += 1
                r = l
            else:
                r += 1
            if r >= len(temperatures):
                res.append(0)
                l+=1
                r = l
        return res