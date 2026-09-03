class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_string = ''.join(ch for ch in s if ch.isalnum()).lower()
        start_index = 0
        end_index = len(clean_string) - 1
        
        while start_index <= end_index:
            if clean_string[start_index] != clean_string[end_index]:
                return False
            start_index = start_index + 1
            end_index = end_index - 1
        
        return True