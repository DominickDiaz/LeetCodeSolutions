class Solution:
    def maxProfit(self, prices: List[int]) -> int:
    
        mostProfit = 0
        minVal = 10000000
        
        profit = 0
        
        for i in prices:
            profit = i - minVal
            if mostProfit < profit:
                mostProfit = profit
            
            minVal = min(i, minVal)
            
        return mostProfit