class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s2) < len(s1):
            return False

        s1_freq = [0] * 26
        for c in s1:
            s1_freq[ord(c) - ord('a')] += 1

        s2_freq = [0] * 26
        l = 0
        for r in range(len(s1)):
            s2_freq[ord(s2[r]) - ord('a')] += 1

        while r < len(s2) - 1:

            if s1_freq == s2_freq:
                return True
            
            s2_freq[ord(s2[l]) - ord('a')] -= 1
            l += 1
            r += 1
            s2_freq[ord(s2[r]) - ord('a')] += 1

        if s1_freq == s2_freq:
            return True
        
        return False
