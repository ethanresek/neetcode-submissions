class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        longest = set()
        nums_set = set(nums)

        for i, curr in enumerate(nums):
            if curr - 1 in nums_set:
                continue
            curr_longest = {curr}
            while curr + 1 in nums_set:
                curr = curr + 1
                curr_longest.add(curr)
            if len(curr_longest) > len(longest):
                longest = curr_longest
        
        return len(longest)