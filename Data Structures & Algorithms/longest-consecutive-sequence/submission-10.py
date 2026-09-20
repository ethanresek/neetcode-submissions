class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        longest = set()
        nums_set = set(nums)

        for num in nums:
            if num - 1 in nums_set:
                continue
            curr_longest = set([num])
            while num + 1 in nums_set:
                num += 1
                curr_longest.add(num + 1)
            if len(curr_longest) > len(longest):
                longest = curr_longest
        
        return len(longest)
            