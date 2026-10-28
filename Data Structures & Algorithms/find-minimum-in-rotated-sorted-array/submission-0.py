class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l = 0
        r = len(nums) - 1

        while l <= r:

            i = l + ((r - l) // 2)

            if nums[l] <= nums[i] and nums[r] >= nums[i]:
                return nums[l]
            elif nums[l] <= nums[i] and nums[r] <= nums[i]:
                l = i + 1
            elif nums[l] >= nums[i] and nums[r] >= nums[i]:
                r = i
        
        return -1
