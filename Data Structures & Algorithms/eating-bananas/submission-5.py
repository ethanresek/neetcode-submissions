class Solution:

    def ceiling(self, num: float):
        return -(-num // 1)

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        
        l = 1
        r = max(piles)
        best_rate = r

        while l <= r:
            
            rate = l + ((r - l) // 2)
            elapsed = 0
        
            for pile in piles:
                time_to_eat = pile / rate
                elapsed += self.ceiling(time_to_eat)

            if elapsed > h:
                l = rate + 1
            else:
                if rate < best_rate:
                    best_rate = rate
                r = rate - 1
        
        return best_rate


