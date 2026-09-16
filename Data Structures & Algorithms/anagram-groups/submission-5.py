class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = {}

        for s in strs:
            anagrams.setdefault("".join(sorted(s)), []).append(s)
        
        return [val for val in anagrams.values()]
