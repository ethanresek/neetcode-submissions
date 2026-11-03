class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
            left_mins = [0] * len(prices)
            right_maxes = [0] * len(prices)

            left_mins[0] = prices[0]
            right_maxes[len(prices) - 1] = prices[len(prices) - 1]

            for i in range(1, len(prices)):
                left_mins[i] = min(left_mins[i - 1], prices[i])
            for i in range(len(prices) - 2, -1, -1):
                right_maxes[i] = max(right_maxes[i + 1], prices[i])
            
            best = 0

            for i in range(len(prices)):
                best = max(best, right_maxes[i] - left_mins[i])
            return best