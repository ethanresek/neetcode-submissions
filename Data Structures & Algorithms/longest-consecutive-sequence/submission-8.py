class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums_set = set(nums)
        result = set()

        for n in nums:

            if n - 1 in result:
                continue
            curr_set = set([n])
            while n + 1 in nums_set:
                n = n + 1
                curr_set.add(n)
            if len(curr_set) > len(result):
                result = curr_set
        
        return len(result)