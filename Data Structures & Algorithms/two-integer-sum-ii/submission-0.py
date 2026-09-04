from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        point1, point2 = 0, len(numbers) - 1
        
        while point1 < point2:
            sumation = numbers[point1] + numbers[point2]
            if  sumation == target:
                return [point1 + 1 , point2 + 1]
            elif sumation > target:
                point2 = point2 - 1
            else:
                point1 = point1 + 1
        
        return None