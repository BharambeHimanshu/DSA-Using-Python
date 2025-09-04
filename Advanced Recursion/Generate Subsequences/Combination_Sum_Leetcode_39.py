# Combination Sum
# Leetcode 39
'''
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.
The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.
The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

Example 1:
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

Example 2:
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

Example 3:
Input: candidates = [2], target = 1
Output: []
'''

class Solution:
    def solve(self, index, total, subset, nums, target, result):
        # Base case: If the running total matches the target, record the current subset
        if total == target:
            result.append(subset.copy())  # Add a copy to avoid future modifications
            return
        # Pruning: If the running total exceeds the target, stop this path
        elif total > target:
            return
        # Base case: If we have considered all candidates, terminate this branch
        if index >= len(nums):
            return

        # Choice 1: Include the candidate at the current index (allowing reuse)
        Sum = total + nums[index]
        subset.append(nums[index])
        self.solve(index, Sum, subset, nums, target, result)  # Same index for reuse

        # Backtrack: Remove the candidate just added
        Sum = total  # Reset Sum to the value before including the candidate
        subset.pop()

        # Choice 2: Skip the candidate and move to the next index
        self.solve(index + 1, Sum, subset, nums, target, result)

    def combinationSum(self, nums, target):
        result = []
        self.solve(0, 0, [], nums, target, result)
        return result
    
solution = Solution()
nums = [2,3,6,7]
target = 7
print(solution.combinationSum(nums,target))