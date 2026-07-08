"""
Input: array of strings
Output: Nested array in which the inner arrays contain anagrams
Edge cases: empty array, single empty string, single example

Plan
- Create dictionary of letter counts to words
- Loop through each word
    - Create a length 26 array per word (for each letter in alphabet)
    - Convert array to tuple once letters are counted
    - Use tuple as key and word arrays as value in dict
- Join each value array and return
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = {}

        for s in strs:

            counts = [0] * 26

            for c in s:
                counts[ord(c) - ord('a')] += 1
            
            anagrams.setdefault(tuple(counts), []).append(s)
        
        return list(anagrams.values())