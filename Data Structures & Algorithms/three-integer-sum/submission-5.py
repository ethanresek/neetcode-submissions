class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i, n in enumerate(nums):
            l, r = i + 1, len(nums) - 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            while l < r:
                total = nums[r] + nums[l]

                if total > -n:
                    r -= 1
                elif total < -n:
                    l += 1
                else:
                    res.append([nums[r], nums[l], n])
                    r -= 1
                    l += 1
                    while l < r and nums[l - 1] == nums[l]:
                        l += 1
            
        return res