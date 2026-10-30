class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if len(t) > len(s):
            return ""
        
        t_freq = defaultdict(int)
        for c in t:
            t_freq[c] += 1
        
        s_freq = defaultdict(int)
        have = 0
        need = len(t_freq)

        l = 0
        r = 0
        output = ""

        while r < len(s):

            while r < len(s) and have != need:
                s_freq[s[r]] += 1
                if s_freq[s[r]] == t_freq[s[r]]:
                    have += 1
                r += 1
            
            if r >= len(s) and have != need:
                return output
            
            while l < r and have == need:
                s_freq[s[l]] -= 1
                if s_freq[s[l]] < t_freq[s[l]]:
                    have -= 1
                l += 1
            
            sub = s[l - 1 : r]
            print(sub)
            if not output or len(sub) < len(output):
                output = sub
            
        return output
