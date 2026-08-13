from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str: str = ""
        
        for element in strs:
            encoded_str =encoded_str + str(len(element)) + "#" + element
        
        return encoded_str
        
        
        
    def decode(self, s: str) -> List[str]:
        true_list: List = []
        i = 0
        while i < len(s):
            hash_position = s.index("#", i)
            length = int(s[i:hash_position])
            word = s[hash_position+1 : hash_position+1+length]
            true_list.append(word)
            i = hash_position + 1 + length
            
        return true_list