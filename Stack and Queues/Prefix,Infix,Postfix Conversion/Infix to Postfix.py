# Infix to Postfix       TC -> o(n)+o(n)              SC -> o(n)+o(n)

class Solution:
    def priority(self, ch):
        # Define operator priority hierarchy
        if ch == "+" or ch == "-": # Lowest
            return 1
        if ch == "*" or ch == "/":
            return 2
        if ch == "^":              # Highest 
            return 3
        return 0  # For non-operators like '(' and ')'     aur agar uper ke tino mai se nahi hai to sabse lowest

    def InfixtoPostfix(self, s):
        stack = []    # Stack to help with operator ordering
        result = []   # To store the postfix expression

        for char in s:
            # If character is an operand, add it directly to result
            if ("a" <= char <= "z") or ("A" <= char <= "Z") or ("0" <= char <= "9"):
                result.append(char)
           
            # If character is '(', push it to the stack
            elif char == "(":
                stack.append(char)
           
            # If character is ')', pop until '(' is encountered
            elif char == ")":
                while stack and stack[-1] != "(":
                    result.append(stack.pop())
                stack.pop()  # Discard the '('
           
            # If character is an operator
            else:
                # Pop operators with higher or equal priority
                while stack and self.priority(stack[-1]) >= self.priority(char):
                    result.append(stack.pop())
                stack.append(char)  # Push current operator

        # Pop remaining operators from the stack
        while stack:
            result.append(stack.pop())

        return "".join(result)  # Convert list to string

sol = Solution()
print(sol.InfixtoPostfix("A+B*(C^D-E)"))
