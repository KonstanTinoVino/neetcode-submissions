from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        
        return "".join(str(len(x)) + "#" + x for x in strs)
    
    def decode(self, s: str) -> List[str]:
        final_array = []
        i = 0
        while i < len(s):
            hash = s.index("#", i)
            word_length = s[i: hash]
            word = s[hash+1:hash+1+int(word_length)]
            final_array.append(word)
            i = 1 + hash + int(word_length)
        return final_array