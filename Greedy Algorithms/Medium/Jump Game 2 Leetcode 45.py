'''
You are given a 0-indexed array of integers nums of length n. You are initially positioned at index 0.
Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at index i, you can jump to any index (i + j) where:
0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach index n - 1. The test cases are generated such that you can reach index n - 1.

Example 1:
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [2,3,0,1,4]
Output: 2
'''

# Brute Force Using Recursion          TC ->o(n^n)    SC -> o(n)
class Solution:
    def solve(self, index, jump, lastIndex, nums):
        if index >= lastIndex:
            return jump
        minJump = float("inf")
        for i in range(1, nums[index] + 1):
            minJump = min(minJump, self.solve(index + i, jump + 1, lastIndex, nums))
        return minJump

    def jump(self, nums):
        return self.solve(0, 0, len(nums) - 1, nums)
    
sol = Solution()
print(sol.jump([2,3,0,1,4]))


# Optimal Using Greedy Algorithm
class Solution:
    def jump(self, nums):
        n = len(nums)
        jumps = 0
        left = 0
        right = 0
        while right < n - 1:
            farthest = 0
            for i in range(left, right + 1):
                farthest = max(farthest, i + nums[i])     # i + nums[i] -> 0 + 2
            left = right + 1
            right = farthest
            jumps += 1
        return jumps
    
sol = Solution()
print(sol.jump([2,3,0,1,4]))