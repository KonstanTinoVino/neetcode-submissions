from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        element_map = {}
        buckets = [[] for _ in range(len(nums)+1)]
        
        for element in nums:
            element_map[element] = element_map.get(element, 0) + 1
        
        for key, value in element_map.items():
            buckets[value].append(key)
            
        result = []
        for i in range(len(buckets)-1, -1, -1):
            for element in buckets[i]:
                result.append(element)
                if len(result) == k:
                    return result

        return result
    
    
    
