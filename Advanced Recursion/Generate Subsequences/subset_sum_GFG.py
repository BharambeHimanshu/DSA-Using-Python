# Subset Sum
# GeekforGeeks Problem
'''
Input: arr[] = [2, 3]
Output: [0, 2, 3, 5]
Explanation: When no elements are taken then Sum = 0. When only 2 is taken then Sum = 2. When only 3 is taken then Sum = 3. When elements 2 and 3 are taken then Sum = 2+3 = 5.

Input: arr[] = [1, 2, 1]
Output: [0, 1, 1, 2, 2, 3, 3, 4]
Explanation: The possible subset sums are 0 (no elements), 1 (either of the 1's), 2 (the element 2), and their combinations.

Input: arr[] = [5, 6, 7]
Output: [0, 5, 6, 7, 11, 12, 13, 18]
Explanation: The possible subset sums are 0 (no elements), 5, 6, 7, and their combinations.
'''
# Approach would be same pick and not pick

# Brute force Solution
# Using index,total,subset

class Solution:
    def solve(self, nums, index, subset, result):
        # Base case: processed all elements
        if index >= len(nums):
            result.append(sum(subset))  # Calculate sum of current subset
            return
        
        # Choice 1: Include current element
        subset.append(nums[index])
        self.solve(nums, index + 1, subset, result)
        
        # Backtrack: Remove current element  
        subset.pop()
        
        # Choice 2: Exclude current element
        self.solve(nums, index + 1, subset, result)

    def subsetSums(self, nums):
        result = []
        self.solve(nums, 0, [], result)
        result.sort()  # Sort as required by problem
        return result

solution = Solution()
nums = [1,2,3]
print(solution.subsetSums(nums))


# Optimal Solution 
# Without using subset
class Solution:
    def backtrack(self,index,total,result,nums):
        if index >= len(nums):
            result.append(total)
            return
        sum = total + nums[index]
        self.backtrack(index+1,sum,result,nums)
        sum = total
        self.backtrack(index+1,sum,result,nums)
    def subsetsum(self,nums):
        result = []
        self.backtrack(0,0, result,nums)
        result.sort()
        return result

solution = Solution()
nums = [1,2,3,4]
print(solution.subsetsum(nums))

