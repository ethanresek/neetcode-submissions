# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value

class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        
        if len(pairs) < 1:
            return []
        
        end = 0
        out = []
        
        for old in range(1, len(pairs)):
            out.append(pairs.copy())
            i = 0

            for new in range(old):
                
                if pairs[old].key >= pairs[new].key:
                    i+= 1
                else:
                    pairs.insert(i, pairs.pop(old))
                    break

        out.append(pairs.copy())
        return out






