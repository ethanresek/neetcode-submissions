class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}

        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        
        freq_sorted = sorted(freq.items(), key=lambda item: item[1], reverse=True)

        out = []

        for i in range(k):
            out.append(freq_sorted[i][0])
        
        return out