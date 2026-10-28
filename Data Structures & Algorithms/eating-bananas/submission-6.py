class Solution:

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l = 1
        r = max(piles)

        while l <= r:
            
            rate = l + ((r - l) // 2)
            elapsed = 0
        
            for pile in piles:
                time_to_eat = (pile + rate - 1) // rate
                elapsed += time_to_eat
                if elapsed > h:
                    break

            if elapsed > h:
                l = rate + 1
            else:
                r = rate - 1
        
        return l


