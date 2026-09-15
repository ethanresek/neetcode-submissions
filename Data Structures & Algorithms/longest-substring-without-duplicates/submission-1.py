class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) < 2:
            return len(s)

        l = 0
        r = 0
        longest = ""

        while r != len(s):
            character_set = set(s[l:r])
            while r != len(s) and s[r] not in character_set:
                character_set.add(s[r])
                r += 1
            curr_longest = s[l : r]

            if len(curr_longest) > len(longest):
                longest = curr_longest
            
            while r != len(s) and s[l] != s[r]:
                l += 1
            l += 1
        
        print(longest)
        return len(longest)
