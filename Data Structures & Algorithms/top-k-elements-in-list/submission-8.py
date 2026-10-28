class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1
        
        freq_list = sorted(freq.items(), key=lambda x: -x[1])

        output = []

        for i in range(k):
            output.append(freq_list[i][0])

        return output

