# Postfix to Infix Conversion      TC -> o(N)      SC -> o(N)

class Solution:
    def postToInfix(self, s):
        # Stack to store operands or partial infix expressions
        stack = []

        for char in s:
            # If character is an operand (letter or digit), push it to the stack
            if char.isalnum():                                               # isalnum is a method to display A-Z,a-z,0-9
                stack.append(char)
            else:
                # If character is an operator, pop two operands
                operand2 = stack.pop()  # Second operand (popped first)
                operand1 = stack.pop()  # First operand (popped second)

                # Combine operands with the operator, surrounded by parentheses
                new_expr = f"({operand1}{char}{operand2})"

                # Push the resulting expression back onto the stack
                stack.append(new_expr)

        # The final element in the stack is the complete infix expression
        return stack[-1]

sol = Solution()
print(sol.postToInfix("AB-DE+F*/"))