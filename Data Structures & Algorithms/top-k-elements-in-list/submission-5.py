class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}

        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        
        freq_sorted = sorted(freq.items(), key=lambda x: -x[1])

        output = []
        for i in range(k):
            output.append(freq_sorted[i][0])
        
        return output