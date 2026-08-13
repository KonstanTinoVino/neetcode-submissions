from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        table = {}
        for value in strs:
            key = str(sorted(list(value)))
            existing: List = table.get(key, None)
            if existing:
                existing.append(value)
            else:
                existing = [value]
            table[key] = existing
        return list(table.values())