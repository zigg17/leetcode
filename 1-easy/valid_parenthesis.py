class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        ref_dict = {
            "}" : "{",
            "]" : "[" ,
            ")" : "("
        }

        for x in s:
            if x in ref_dict:
                if not stack:
                    return False
                    
                if (ref_dict[x] == stack[-1]):
                    stack.pop()
                else:
                    return False
            else:
                stack.append(x)
            
        if len(stack) == 0:
            return True
        else:
            return False

def run_tests():
    solution = Solution()
    
    test_cases = [
        ("()", True),
        ("({[]})", True),
        ("(]", False),
        ("([)]", False),
        ("", True),
        ("((())", False)
    ]
    
    for i, (input_str, expected) in enumerate(test_cases):
        result = solution.isValid(input_str)
        print(f"Test Case {i + 1}: {'Passed' if result == expected else 'Failed'} - Input: {input_str}, Expected: {expected}, Got: {result}")

# Run the test cases
run_tests()

