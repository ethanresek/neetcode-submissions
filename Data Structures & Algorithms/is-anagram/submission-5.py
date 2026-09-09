class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_freq = {}
        t_freq = {}
        for c in s:
            s_freq[c] = s_freq.get(c, 0) + 1
        for c in t:
            t_freq[c] = t_freq.get(c, 0) + 1


        for key, value in s_freq.items():
            if key not in t_freq or t_freq[key] != value:
                return False
        for key, value in t_freq.items():
            if key not in s_freq or s_freq[key] != value:
                return False
        
        return True