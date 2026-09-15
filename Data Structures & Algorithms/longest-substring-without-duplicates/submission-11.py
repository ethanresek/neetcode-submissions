class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) < 2:
            return len(s)

        l = 0
        r = 0
        longest = 1
        character_set = set()

        while r < len(s):
            while r < len(s) and s[r] not in character_set:
                character_set.add(s[r])
                r += 1
            if r - l > longest:
                longest = r - l
            while l < len(s) and r < len(s) and s[l] != s[r]:
                character_set.remove(s[l])
                l += 1
            l += 1
            r += 1
        
        return longest
