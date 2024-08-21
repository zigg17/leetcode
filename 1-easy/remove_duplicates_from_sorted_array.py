from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        num_dict = {}
        for num in nums:
            if num not in num_dict:
                num_dict[num] = True
        
        unique_keys = list(num_dict.keys())

        for x in range(len(unique_keys)):
            nums[x] = unique_keys[x]
        
        return len(unique_keys)

Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4])

