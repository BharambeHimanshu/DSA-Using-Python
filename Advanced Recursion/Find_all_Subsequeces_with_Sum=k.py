# Find all Subsequences with sum = k
# Geekforgeeks Problem 
# problem statement:- Find the subsequences whose value is equal to the target
'''
Input: arr[] = [1, 2, 3], k = 3 
Output: [ [1, 2], [3] ]
Explanation: All the subsequences of the given array are:
[ [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3], [] ]
Out of which only two subsequences have sum of their elements equal to 3.

Input: arr[] = [1, 2, 3], k = 7
Output: []
Explanation: Sum of all the elements of the array is 6, which is smaller than the required sum, thus they are no subsequences with sum of its elements equal to 7.

Input: arr[] = [17, 18, 6, 11, 2, 4], k = 6  
Output: [ [2, 4], [6] ] 
'''
# Approach would be same as 'all subsequence problem' but here we add one more extra variable called target

def backtrack(subset,index,total):
    # Base case: If sum equals K, add a copy of the subset to result
    if total == target:
        result.append(subset.copy())
        return
    # Prune: If sum exceeds K, stop this path
    elif total > target:
        return
    # Base case: If index is out of bounds, stop
    if index >= len(nums):
        return
    
    # Choice 1: Include the current element
    subset.append(nums[index])  # Add to subset
    Sum = total + nums[index]   # Update sum
    backtrack(subset, index + 1, Sum)  # Recurse to next index
    
    # Backtrack: Undo the inclusion
    subset.pop()                # Remove last element
    Sum = total                 # Reset sum
    
    # Choice 2: Exclude the current element
    backtrack(subset, index + 1, Sum)  # Recurse without adding


result = []                     # List to store all valid subsequences
nums = [1, 2, 3, 4, 3, 2, 1, 1, 1, 1]  # Example array
target = 3                           # Target sum
backtrack([], 0, 0)             # Start backtracking
print(result)                   # Print the result