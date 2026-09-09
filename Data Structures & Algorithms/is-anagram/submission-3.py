class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_freq = {}
        t_freq = {}
        for i in range(len(s)):
            s_freq[s[i]] = s_freq.get(s[i], 0) + 1
            t_freq[t[i]] = t_freq.get(t[i], 0) + 1


        for key, value in s_freq.items():
            if key not in t_freq or t_freq[key] != value:
                return False
        for key, value in t_freq.items():
            if key not in s_freq or s_freq[key] != value:
                return False
        
        return True