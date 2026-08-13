class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        map_s = {}
        map_t = {}
        
        for letter in range(len(s)):
            map_s[str(s[letter])] = map_s.get(str(s[letter]), 0)+ 1
            map_t[str(t[letter])] = map_t.get(str(t[letter]), 0) + 1
        return map_s == map_t