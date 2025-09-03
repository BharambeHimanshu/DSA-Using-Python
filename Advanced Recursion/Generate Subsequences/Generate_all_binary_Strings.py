# Generate all binary strings 
# GeekforGeeks Problem

'''
Example 1:
Input:
N = 3
Output:
000 , 001 , 010 , 100 , 101
Explanation:
None of the above strings contain consecutive 1s. "110" is not an answer as it has '1's occuring consecutively. 
'''

class Solution:
    def solve(self, index, flag, numbers, result):
        # Base case: If we've filled all positions, add to result
        if index >= len(numbers):
            result.append("".join(numbers))  # Convert array to string  ("0","1","0") -> "010"
            return
        
        # Choice 1: Always place '0' at current position
        numbers[index] = "0"
        self.solve(index + 1, True, numbers, result)  # Next position can have 0 or 1
        
        # Choice 2: Place '1' only if flag is True (no consecutive 1's)
        if flag == True:
            numbers[index] = "1"
            self.solve(index + 1, False, numbers, result)  # Next position can only have 0
            numbers[index] = "0"  # Backtrack: reset to "0" for clean slate

    def generateBinaryStrings(self, n):
        numbers = ["0"] * n  # Initialize array with all "0"s
        result = []          # List to store all valid binary strings
        self.solve(0, True, numbers, result)  # Start from index 0, flag=True
        return result
solution = Solution()
n = 3
print(solution.generateBinaryStrings(n))