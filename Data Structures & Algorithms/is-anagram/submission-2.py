class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        s_freq = {}
        t_freq = {}
        for i in range(len(s)):
            s_freq[s[i]] = s_freq.get(s[i], 0) + 1
            t_freq[t[i]] = t_freq.get(t[i], 0) + 1
        
        s_items = sorted(s_freq.items())
        t_items = sorted(t_freq.items())

        if len(s_items) != len(t_items):
            return False

        for i in range(len(s_items)):
            if s_items[i] != t_items[i]:
                return False
        
        return True