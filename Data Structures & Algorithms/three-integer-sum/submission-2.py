class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()

        matches = set()

        for i, val in enumerate(nums):
            j = 0
            k = len(nums) - 1

            while j < k:

                if j == i or nums[j] + nums[k] < -val:
                    j += 1
                elif k == i or nums[j] + nums[k] > -val:
                    k -= 1
                else:
                    matches.add(tuple(sorted([nums[j], nums[k], val])))
                    j += 1
                    k -= 1

        
        return list(matches)
                    
