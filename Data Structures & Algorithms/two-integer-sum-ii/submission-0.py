class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        for i, i_val in enumerate(numbers):
            for j, j_val in enumerate(numbers):

                if i == j:
                    continue
                if i_val + j_val == target:
                    return [i + 1, j + 1]
        
        return []