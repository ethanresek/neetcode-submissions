"""
- Create two hash maps for s and t
- t hashmap is constant, s is tracked with the growth and shrinking of a window
- start with indexes l and r at index 0.
- Keep track of 
- Once 
"""
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(s) < len(t):
            return ""

        t_map = {}
        for c in t:
            t_map[c] = t_map.get(c, 0) + 1
        s_window = {}

        need = len(set(t))
        have = 0

        l = 0
        r = 0

        out = ""

        while r < len(s):

            while r < len(s) and have != need:
                if s[r] in t_map:
                    s_window[s[r]] = s_window.get(s[r], 0) + 1
                    if s_window[s[r]] == t_map[s[r]]:
                        have += 1
                r += 1

            if r == len(s) and have != need:
                break

            while l < r and have == need:
                if s[l] in t_map:
                    s_window[s[l]] = s_window.get(s[l], 0) - 1
                    if s_window[s[l]] < t_map[s[l]]:
                        have -= 1
                l += 1
            
            sub = s[l - 1 : r]
            if not out or len(sub) < len(out):
                out = sub
        
        return out

            