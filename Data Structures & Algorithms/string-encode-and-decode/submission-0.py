class Solution:

    def encode(self, strs: List[str]) -> str:
        
        encoded = ""

        for s in strs:
            encoded += f"{len(s)}#{s}"
        return encoded


    def decode(self, s: str) -> List[str]:
        
        strs = []

        i = 0
        while i < len(s):
            
            length = ""
            while s[i] != '#':
                length += s[i]
                i += 1
            print(length)
            length = int(length) if length else 0

            i += 1
            decoded = ""
            for _ in range(length):
                decoded += s[i]
                i += 1
            
            strs.append(decoded)
        
        return strs



