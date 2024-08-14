class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {
            "I" : 1, "V" : 5, "IV" : 4,
            "X" : 10, "IX" : 9, "L" : 50,
            "XL" : 40, "C" : 100, "XC" : 90,
            "D" : 500, "CD" : 400, "M" : 1000,
            "CM" : 900
        }

        final = 0
        while s:
            if(len(s) == 1):
                final += roman_dict[s[0]]
                return final
            if roman_dict[s[1]] > roman_dict[s[0]]:
               final += roman_dict[s[0:2]]
               s = s[2:]
            else:
                final += roman_dict[s[0]]
                s = s[1:]
        return final
            
            

solution = Solution()
print(solution.romanToInt("MCMXCIV"))