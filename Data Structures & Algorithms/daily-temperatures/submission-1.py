class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        output = []

        for i, temp in enumerate(temperatures):

            j = i + 1
            dist = 1

            while j < len(temperatures) and temp >= temperatures[j]:
                j += 1
                dist += 1
            
            if j == len(temperatures):
                output.append(0)
            else:
                output.append(dist)
        
        return output