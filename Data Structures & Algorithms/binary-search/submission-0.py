class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l = 0
        r = len(nums) - 1
        i = len(nums) // 2

        while l <= r:

            if nums[i] == target:
                return i
            
            if nums[i] > target:
                r = i - 1
            else:
                l = i + 1

            i = (r + l) // 2

        
        return -1
        