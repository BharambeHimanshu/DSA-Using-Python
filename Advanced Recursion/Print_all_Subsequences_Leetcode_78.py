# Print all the subsequences using Recursion
#Leetcode 78

'''
Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
Input: nums = [0]
Output: [[],[0]]
'''

# Approach
'''
1. Recursive Function: We create a helper function solve that takes the current index in the array, the current subset being built, the original array, and the result list.
2. Base Case: If the index reaches the end of the array (we've made choices for all elements), add a copy of the current subset to the result.
3. Include Choice: Add the current element to the subset, then recurse to the next index.
4. Backtrack: After exploring the “include” path, remove the last element (pop it) to undo the choice.
5. Exclude Choice: Recurse to the next index without adding the current element.
6. Start Recursion: Call the function with index 0 and an empty subset.
7. Return Result: The result list will contain all subsets.
'''

class Solution:
    def solve(self, index, subset, nums, result):
        # Base case: We've processed all elements, add current subset to result
        if index >= len(nums):
            result.append(subset.copy())  # Use copy to avoid modifying later
            return
        
        # Choice 1: Include the current element in the subset
        subset.append(nums[index])    # Add to current subset
        self.solve(index + 1, subset, nums, result)  # Recurse to next index
        
        # Backtrack: Undo the inclusion to try the exclude choice
        subset.pop()                  # Remove the last added element
        
        # Choice 2: Exclude the current element
        self.solve(index + 1, subset, nums, result)  # Recurse without adding

    def subsets(self, nums):
        result = []                   # List to store all subsets
        self.solve(0, [], nums, result)  # Start from index 0 with empty subset
        return result

nums = [1, 2, 3]
solution = Solution()
result = solution.subsets(nums)
print(result)
