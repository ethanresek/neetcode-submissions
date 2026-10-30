class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0

        for i, n in enumerate(nums):
            if n - 1 in nums_set:
                continue
            curr = 1
            while n + 1 in nums_set:
                n = n + 1
                curr += 1
            if curr > longest:
                longest = curr
        
        return longest