from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack_temps = []
        count_temps = [0] * len(temperatures)
        
        for i, t in enumerate(temperatures):
            while stack_temps and t > stack_temps[-1][0]:
                stackT, stackInd = stack_temps.pop()
                count_temps[stackInd] = i - stackInd
            stack_temps.append((t, i))
        return count_temps
                