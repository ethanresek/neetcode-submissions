class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False
        
        s1_freq = defaultdict(int)
        for c in s1:
            s1_freq[c] += 1
        
        s2_freq = defaultdict(int)
        for i in range(len(s1)):
            s2_freq[s2[i]] += 1

        print(s1_freq, s2_freq)

        l = 0
        r = len(s1) - 1

        while r < len(s2) - 1:

            if s1_freq == s2_freq:
                return True

            s2_freq[s2[l]] -= 1
            if s2_freq[s2[l]] <= 0:
                del s2_freq[s2[l]]
            l += 1
            
            r += 1
            s2_freq[s2[r]] += 1
        
        if s1_freq == s2_freq:
            return True
        
        return False

        
