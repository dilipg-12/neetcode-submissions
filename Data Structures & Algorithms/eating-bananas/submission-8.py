class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)
        sol = []
        while l<=r:
            m = (l+r)//2
            print(l,r,m)
            eats = 0
            for ban in piles:
                eats+= -(-ban // m)
            # print(eats, m)
            if eats > h:
                l = m +1
            elif eats<=h:
                r = m - 1
                sol.append(m)
        return min(sol)