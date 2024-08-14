class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        ref_dict = {
            "}" : "{",
            "]" : "[",
            ")" : "("
        }
        for x in s:
            pass




solution = Solution()
print(solution.isValid("{}"))