class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        left_min = [prices[0]] * len(prices)
        right_max = [prices[-1]] * len(prices)

        for i in range(1, len(left_min)):
            left_min[i] = min(left_min[i - 1], prices[i])
        for i in range(len(left_min) - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], prices[i])
        
        highest = 0

        for i in range(len(prices)):
            profit = right_max[i] - left_min[i]
            if profit > highest:
                highest = profit

        return highest