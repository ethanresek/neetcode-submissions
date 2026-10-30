class Solution:

    def encode(self, strs: List[str]) -> str:

        output = ""
        for s in strs:
            output += f"{len(s)}#{s}"
        return output

    def decode(self, s: str) -> List[str]:

        i = 0
        output = []
        while i < len(s) - 1:

            length = ""
            while s[i].isdigit():
                length += s[i]
                i += 1
            length = int(length)
            i += 1
            endpoint = i + length
            new_string = ""
            while i < endpoint:
                new_string += s[i]
                i += 1
            output.append(new_string)

        return output