class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = float('inf')
        for p in prices:
            if buy > p:
                buy = p
            else:
                profit = max(profit, p - buy)
        return profit
        