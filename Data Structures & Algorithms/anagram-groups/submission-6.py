class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = {}

        for s in strs:
            alph = [0] * 26
            for c in s:
                alph[ord(c) - ord('a')] += 1
            alph = tuple(alph)

            groups.setdefault(alph, []).append(s)
        
        return [value for value in groups.values()]