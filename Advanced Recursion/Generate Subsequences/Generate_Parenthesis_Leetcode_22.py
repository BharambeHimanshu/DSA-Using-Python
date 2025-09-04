# Generate Parenthesis
# Leetcode 22
'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]
'''

class Solution:
    def solve(self, index, total, brackets, result):
        # Base case: If we've filled all positions
        if index >= len(brackets):
            if total == 0:  # All brackets are properly matched
                result.append("".join(brackets))  # Add valid combination
            return
        
        # Pruning: Too many unmatched opening brackets      n =2  ((( and this happens
        if total > len(brackets) // 2:
            return
        
        # Pruning: More closing brackets than opening (invalid)           n =2   )-> closing bracket at starting
        if total < 0:
            return
        
        # Choice 1: Place opening bracket '('
        brackets[index] = "("
        Sum = total + 1  # Increment unmatched opening count
        self.solve(index + 1, Sum, brackets, result)
        
        # Choice 2: Place closing bracket ')'
        brackets[index] = ")"
        Sum = total - 1  # Decrement unmatched opening count
        self.solve(index + 1, Sum, brackets, result)

    def generateParenthesis(self, n):
        brackets = [""] * (n * 2)  # Array of size 2n for n pairs
        result = []                # List to store all valid combinations
        self.solve(0, 0, brackets, result)  # Start with index 0, total 0
        return result
    
solution = Solution()
n = 3
print(solution.generateParenthesis(n))