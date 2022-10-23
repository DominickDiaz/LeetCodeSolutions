class Solution:
    def maxProfit(self, prices: List[int]) -> int:
    
        if not prices:
            return 0

        low = 0
        max_profit = 0

        for i in range(len(prices)):
            if prices[i] < prices[low]:
                low = i
            else:
                max_profit = max(max_profit, prices[i] - prices[low])

        return max_profit