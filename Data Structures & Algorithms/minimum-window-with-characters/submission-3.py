class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if len(s) < len(t):
            return ""

        t_freq = defaultdict(int)
        for c in t:
            t_freq[c] += 1

        need = len(set(t))
        have = 0
        
        s_freq = defaultdict(int)
        l, r = 0, 0

        out = ""

        while r < len(s):

            while r < len(s) and have != need:
                if s[r] in t_freq:
                    s_freq[s[r]] += 1
                    if s_freq[s[r]] == t_freq[s[r]]:
                        have += 1
                r += 1
            
            if r >= len(s) and have != need:
                break

            while l < r and have == need:
                if s[l] in t_freq:
                    s_freq[s[l]] -= 1
                    if s_freq[s[l]] < t_freq[s[l]]:
                        have -= 1
                l += 1

            sub = s[l - 1 : r]
            if not out or len(sub) < len(out):
                out = sub
        
        return out
            
            
            
            
                
