class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        if not s:
            return 0

        freq = {}
        longest = 1
        l = 0
        r = 0

        while r < len(s):
            
            freq[s[r]] = freq.get(s[r], 0) + 1
            max_freq = max(freq.values(), default=0)
            curr_length = r - l + 1

            if max_freq + k >= curr_length:
                if curr_length > longest:
                    longest = curr_length
            else:
                freq[s[l]] -= 1
                l += 1
            
            r += 1

        return longest

        