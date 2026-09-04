class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = {}

        for s in strs:

            counts = [0] * 26
            
            for c in s:

                counts[ord(c) - ord('a')] += 1

            anagrams.setdefault(tuple(counts), []).append(s)
        
        return list(anagrams.values())