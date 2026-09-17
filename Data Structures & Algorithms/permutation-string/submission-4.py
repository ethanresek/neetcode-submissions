"""
Plan:
 - Convert s1 to a tuple
 - Crawl through s2 a three character string at a time
 - if that three character string converted == s1
    - 
"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1 = sorted(list(s1))
        i = 0
        j = len(s1)

        while j <= len(s2):
            if sorted(list(s2[i:j])) == s1:
                return True
            i += 1
            j += 1

        return False

