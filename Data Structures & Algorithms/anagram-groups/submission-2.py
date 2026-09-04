"""
Plan:

"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = {}

        for s in strs:
            clean = "".join(sorted(s))
            groups.setdefault(clean, []).append(s)
        
        out = []

        for arr in groups.values():
            out.append(arr)
        
        return out
