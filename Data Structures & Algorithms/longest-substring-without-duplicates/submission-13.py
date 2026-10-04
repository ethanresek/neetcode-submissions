class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if not s:
            return 0

        present = set()

        l = 0
        r = 0

        longest_length = 1

        while r < len(s):

            while r < len(s) and s[r] not in present:
                present.add(s[r])
                r += 1
            
            if r - l > longest_length:
                longest_length = r - l

            while r < len(s) and s[l] != s[r]:
                present.remove(s[l])
                l += 1

            l += 1
            r += 1
        
        return longest_length

        