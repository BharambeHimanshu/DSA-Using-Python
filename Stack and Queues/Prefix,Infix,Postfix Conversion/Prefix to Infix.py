# Prefix to Infix Conversion
# Same as Postfix to Infix But 1) Reverse iterate   2) And operands ko reverse

class Solution:
    def preToInfix(self, s):
        # Stack to store operands or partial infix expressions
        stack = []

        # Process the prefix expression from right to left
        # Difference here 
        for char in s[::-1]:
            # If character is an operand (letter or digit), push it to the stack
            if char.isalnum():
                stack.append(char)
            else:
                # If character is an operator, pop two operands
                # Difference Here
                operand1 = stack.pop()  # First operand
                operand2 = stack.pop()  # Second operand

                # Combine operands with the operator, surrounded by parentheses
                new_expr = f"({operand1}{char}{operand2})"

                # Push the resulting expression back onto the stack
                stack.append(new_expr)

        # The final element in the stack is the complete infix expression
        return stack[-1]
sol = Solution()
print(sol.preToInfix("*+PQ-MN"))