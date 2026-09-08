class Solution:

    def encode(self, strs: List[str]) -> str:
        
        out = ""
        for s in strs:
            out += f"{len(s)}#{s}"
        
        return out

    def decode(self, s: str) -> List[str]:

        strs = []

        i = 0

        while i < len(s):

            length = ""
            while s[i] != "#":
                length += s[i]
                i += 1
            length = int(length)

            i += 1
            decoded = ""
            for _ in range(length):
                decoded += s[i]
                i += 1
            
            strs.append(decoded)
        
        return strs
        