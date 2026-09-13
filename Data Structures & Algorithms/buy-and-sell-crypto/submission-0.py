class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0

        for i, start in enumerate(prices):
            for end in prices[i + 1:]:
                curr_profit = end - start
                if curr_profit > profit:
                    profit = curr_profit
        
        return profit