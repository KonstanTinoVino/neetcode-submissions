class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        for index, num in enumerate(nums):
            wanted = target - num
            if wanted in table:
                return [table[wanted], index]
            else:
                table[num] = index
                
        return []