"""
Plan:
 - Convert nums into a set
 - Loop through each value in nums
    - if target - val in nums_set return both indices
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}

        for i, num in enumerate(nums):
            p = target - num
            if p in seen:
                return [seen[p], i]
            seen[num] = i