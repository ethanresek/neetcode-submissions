class Solution:

    def encode(self, strs: List[str]) -> str:
        
        encoded = ""
        for s in strs:
            encoded += f"{len(s)}#{s}"
        
        return encoded

    def decode(self, s: str) -> List[str]:
        
        i = 0
        strs = []

        while i < len(s) - 1:

            length = ""
            print(s[i])
            while s[i].isdigit():
                length += s[i]
                i += 1
            print(length)
            length = int(length)
            i += 1
            j = 0
            decoded = ""

            while j < length:
                decoded += s[i]
                i += 1
                j += 1
            
            print(decoded)
            
            strs.append(decoded)
        
        return strs

            
