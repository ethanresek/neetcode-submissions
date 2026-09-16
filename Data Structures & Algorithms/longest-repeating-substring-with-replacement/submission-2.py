class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        if not s:
            return 0

        freq = {}
        l = 0
        r = 0
        longest = 1

        while r < len(s):
            freq[s[r]] = freq.get(s[r], 0) + 1
            max_freq = max(freq.values(), default=0)

            if max_freq + k >= r - l + 1:
                if r - l + 1 > longest:
                    longest = r - l + 1
            else:
                freq[s[l]] -= 1             
                l += 1
        
            r += 1
        
        return longest

            
