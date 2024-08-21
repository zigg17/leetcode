class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        included = []
        counter = 0
        for num in nums:
            if num != val:
                included.append(num)
                counter += 1
        
        for x in range(counter):
            nums[x] = included[x]

        return counter