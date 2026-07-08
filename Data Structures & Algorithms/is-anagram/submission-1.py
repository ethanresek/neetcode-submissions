class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        freq_s = {}
        freq_t = {}

        for c in s:
            freq_s[c] = freq_s.get(c, 0) + 1
        for c in t:
            freq_t[c] = freq_t.get(c, 0) + 1
        
        for key in freq_s:
            if key not in freq_t or freq_s[key] != freq_t[key]:
                return False
        for key in freq_t:
            if key not in freq_s or freq_s[key] != freq_t[key]:
                return False

        return True