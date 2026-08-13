from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        table = {}
        for value in strs:
            hashed = hash(str(sorted(list(value))))
            existing: List = table.get(hashed, None)
            if existing:
                existing.append(value)
            else:
                existing = [value]
            table[hashed] = existing
        return list(table.values())