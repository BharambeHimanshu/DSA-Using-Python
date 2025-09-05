# Combination Sum 2
# Leetcode 40
'''
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.
Each number in candidates may only be used once in the combination.
Note: The solution set must not contain duplicate combinations.

Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

Example 2:
Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
'''

# Brute Force 
# Using pick and not pick approach

class Solution:
    def backtrack(self, subset, index, target, result, candidates):
        # Base case: Found a valid combination
        if target == 0:
            result.add(tuple(subset.copy()))  # Add as tuple to set for deduplication
            return
        # Pruning: Invalid path if target becomes negative
        elif target < 0:
            return
        # Base case: No more candidates to consider
        if index >= len(candidates):
            return
        
        # Choice 1: Include current candidate
        subset.append(candidates[index])
        target -= candidates[index]
        self.backtrack(subset, index + 1, target, result, candidates)  # Move to next index
        
        # Backtrack: Remove the candidate and restore target
        subset.pop()
        target += candidates[index]
        
        # Choice 2: Exclude current candidate
        self.backtrack(subset, index + 1, target, result, candidates)

    def combinationSum2(self, candidates, target):
        candidates.sort()  # Sort to ensure consistent combination generation
        result = set()     # Use set to automatically handle duplicates
        self.backtrack([], 0, target, result, candidates)
        return list(result)  # Convert set of tuples back to list of lists
    
solution = Solution()
candidates = [2,5,2,1,2]
target = 5
print(solution.combinationSum2(candidates,target))


# Optimal Soltion 
# Using Loop
class Solution:
    def backtrack(self, subset, index, target, result, candidates):
        # Base case: Found a valid combination
        if target == 0:
            result.append(subset.copy())  # Add copy to preserve current state
            return
        
        # Try each candidate from current index onwards
        for i in range(index, len(candidates)):
            # Skip duplicates: if current element is same as previous and we're not
            # at the starting position, skip it to avoid duplicate combinations
            if i > index and candidates[i] == candidates[i - 1]:
                continue
            
            # Early termination: if current candidate exceeds target,
            # all remaining candidates will also exceed (array is sorted)
            if candidates[i] > target:
                break
            
            # Include current candidate
            subset.append(candidates[i])
            self.backtrack(subset, i + 1, target - candidates[i], result, candidates)
            
            # Backtrack: remove the candidate
            subset.pop()

    def CombinationSum2(self, candidates, target):
        candidates.sort()  # Sort to enable duplicate skipping and early termination
        result = []
        self.backtrack([], 0, target, result, candidates)
        return result
solution = Solution()
candidates = [1,1,2,1,2]
target = 4
print(solution.CombinationSum2(candidates,target))