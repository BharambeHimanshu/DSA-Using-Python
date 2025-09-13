# Valid Parentheses
# Leetcode 20
'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 
Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([])"
Output: true

Example 5:
Input: s = "([)]"
Output: false
'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for bracket in s:
            # If opening bracket, push to stack
            if bracket in "([{":
                stack.append(bracket)
            else:
                # For closing bracket, stack cannot be empty
                if len(stack) == 0:
                    return False
                
                # Pop last opening bracket and check if matching
                ch = stack.pop()
                if (bracket == ")" and ch == "(") or \
                   (bracket == "]" and ch == "[") or \
                   (bracket == "}" and ch == "{"):
                    continue
                else:
                    return False
        
        # Check if all opened brackets were closed
        return len(stack) == 0

p = Solution()
print(p.isValid("([)]"))