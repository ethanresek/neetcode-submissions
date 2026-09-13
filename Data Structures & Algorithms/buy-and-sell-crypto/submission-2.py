class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        best_buy = [prices[0]]
        best_sell = [0] * len(prices)
        best_sell[len(prices) - 1] = prices[len(prices) - 1]

        for i in range(1, len(prices)):
            best_buy.append(min(best_buy[i - 1], prices[i]))
        
        for i in range(len(prices) - 2, -1, -1):
            best_sell[i] = max(best_sell[i + 1], prices[i])

        print(best_buy)
        print(best_sell)

        max_profit = 0
        for i in range(len(prices)):
            curr_profit = best_sell[i] - best_buy[i]
            if curr_profit > max_profit:
                max_profit = curr_profit
        
        return max_profit


        