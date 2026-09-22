class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        output = [0] * len(temperatures)
        stack = []
        
        for i in range(len(temperatures)):
            
            while stack and temperatures[i] > stack[-1][1]:
                val = stack.pop()
                output[val[0]] = i - val[0]
            stack.append((i, temperatures[i]))

        return output
