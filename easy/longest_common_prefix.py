class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if(len(strs) == 1):
            return strs[0]

        total = ''
        for x in range(len(strs[0]) + 1):
            for string in strs:
                if total != string[:x]:
                    return total[:x-1]

            total = string[:x+1]
        
        return total[:x]

                

solution = Solution()

# Test cases
print(solution.longestCommonPrefix(["", "b"])) 
print(solution.longestCommonPrefix(["flower", "flow", "flight"]))  # Expected output: "fl"
print(solution.longestCommonPrefix(["dog", "racecar", "car"]))     # Expected output: ""
print(solution.longestCommonPrefix(["interspecies", "interstellar", "interstate"]))  # Expected output: "inters"
print(solution.longestCommonPrefix(["throne", "throne"]))  # Expected output: "throne"
print(solution.longestCommonPrefix(["throne", "dungeon"]))  # Expected output: ""
print(solution.longestCommonPrefix(["throne", "thrones"]))  # Expected output: "throne"
print(solution.longestCommonPrefix(["single"]))  # Expected output: "single"
