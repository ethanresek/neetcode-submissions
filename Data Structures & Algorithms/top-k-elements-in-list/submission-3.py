
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}
        buckets = [[] for _ in range(len(nums))]
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        for key, val in freq.items():
            buckets[val - 1].append(key)
        out = []
        i = len(buckets) - 1
        
        while i >= 0:

            for num in buckets[i]:
                print(num)
                out.append(num)
                k -= 1
                if k == 0:
                    return out
            
            i -= 1
            
        
