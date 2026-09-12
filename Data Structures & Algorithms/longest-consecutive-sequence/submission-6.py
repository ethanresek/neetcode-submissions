class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        
        nums_set = set(nums)
        final_set = set()

        for val in nums:
            if val + 1 in nums_set and val not in final_set:
                curr_set = set()
                while val in nums_set:
                    curr_set.add(val)
                    val += 1
                if len(curr_set) > len(final_set):
                    final_set = curr_set

        if nums and not final_set:
            return 1
        
        return len(final_set)