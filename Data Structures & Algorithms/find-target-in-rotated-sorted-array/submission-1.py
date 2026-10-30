"""
- if current != target and current window is sorted, split current table based on if current is > or < target
- if current is smaller than both l and r, then split based on if target is > or < l/r
- similar to if current is greater
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums) - 1

        while l <= r:
            
            i = l + ((r - l) // 2)
            l_val = nums[l]
            r_val = nums[r]
            curr = nums[i]

            print(l_val, curr, r_val)

            if target == curr:
                return i
            else:
                if l_val <= curr and r_val > curr:
                    if target < curr:
                        r = i - 1
                    else:
                        l = i + 1
                elif l_val <= curr and r_val < curr:
                    if target > curr:
                        l = i + 1
                    else: # target < curr
                        if target <= r_val:
                            l = i + 1
                        else:
                            r = i - 1
                elif l_val >= curr and r_val > curr:
                    if target < curr:
                        r = i - 1
                    else: # target > curr
                        if target <= r_val:
                            l = i + 1
                        else:
                            r = i - 1
                else:
                    return -1

        return -1