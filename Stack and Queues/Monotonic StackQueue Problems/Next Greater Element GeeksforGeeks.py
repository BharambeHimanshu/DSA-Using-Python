# Next Greater Element 
# GeekforGeeks Problem

'''
You are given an array arr[] of integers, the task is to find the next greater element for each element of the array in order of their appearance in the array. Next greater element of an element in the array is the nearest element on the right which is greater than the current element.
If there does not exist next greater of current element, then next greater element for current element is -1.

Examples

Input: arr[] = [1, 3, 2, 4]
Output: [3, 4, 4, -1]
Explanation: The next larger element to 1 is 3, 3 is 4, 2 is 4 and for 4, since it doesn't exist, it is -1.

Input: arr[] = [6, 8, 0, 1, 3]
Output: [8, -1, 1, 3, -1]
Explanation: The next larger element to 6 is 8, for 8 there is no larger elements hence it is -1, for 0 it is 1, for 1 it is 3 and then for 3 there is no larger element on right and hence -1.

Input: arr[] = [1, 2, 3, 5]
Output: [2, 3, 5, -1]
Explanation: For a sorted array, the next element is next greater element also except for the last element.

Input: arr[] = [5, 4, 3, 1]
Output: [-1, -1, -1, -1]
Explanation: There is no next greater element for any of the elements in the array, so all are -1.
'''

# Brute Force Solution      TC -> o((n*(n+1)//2)      SC -> o(n)

class Solution:
    def nextLargerElement(self, arr):
        n = len(arr)
        ans = [-1] * n    # Initialize all answers as -1
        for i in range(0, n):
            # Check for greater element towards right of arr[i]
            for j in range(i + 1, n):
                if arr[j] > arr[i]:
                    ans[i] = arr[j]   # Set the NGE for arr[i]
                    break   # Stop at the first greater element
        return ans
sol = Solution()
print(sol.nextLargerElement([1,3,2,4]))


# Optimal Solution          TC -> o(2n)     SC ->o(N)

class Solution:
    def nextLargerElement(self, arr):
        n = len(arr)
        result = [-1] * n    # Initialize all answers as -1
        stack = []           # Stack to store potential NGEs
        
        for i in range(n - 1, -1, -1):
            # Remove elements not greater than arr[i]
            while len(stack) != 0 and stack[-1] <= arr[i]:
                stack.pop()
                
            # If stack is not empty, assign top as NGE
            if len(stack) != 0:
                result[i] = stack[-1]
            # Push current element to stack for future comparisons
            stack.append(arr[i])
        return result
sol = Solution()
print(sol.nextLargerElement([1,2,3,5]))