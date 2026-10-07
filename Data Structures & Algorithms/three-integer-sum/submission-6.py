class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, n in enumerate(nums):
            l = i + 1
            r = len(nums) - 1
            
            if i > 0 and n == nums[i - 1]:
                continue
            
            while l < r:
                total = nums[l] + nums[r]

                if total > -n:
                    r -= 1
                elif total < -n:
                    l += 1
                else:
                    res.append([n, nums[l], nums[r]])
                    r -= 1
                    l += 1
                    while l < r and nums[l - 1] == nums[l]:
                        l += 1
        
        return res
                
                