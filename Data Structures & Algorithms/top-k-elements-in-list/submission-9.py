class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = defaultdict(int)

        for n in nums:
            freq[n] += 1
        
        group_freq = defaultdict(list)

        for key, val in freq.items():
            group_freq[val].append(key)
        
        output = []
        i = len(nums)
        while i > 0 and len(output) < k:
            if group_freq[i]:
                for val in group_freq[i]:
                    output.append(val)
                    if len(output) >= k:
                        return output
            i -= 1

        return output