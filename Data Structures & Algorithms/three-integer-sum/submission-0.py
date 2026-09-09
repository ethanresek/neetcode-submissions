class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        triplets = set()

        for i, inum in enumerate(nums):
            for j, jnum in enumerate(nums):
                for k, knum in enumerate(nums):

                    if i == j or j == k or i == k:
                        continue
                    
                    summation = inum + jnum + knum
                    if summation == 0:
                        triplets.add(tuple(sorted((inum, jnum, knum))))

        return list(triplets)