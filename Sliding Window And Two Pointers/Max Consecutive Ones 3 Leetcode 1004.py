# Max Consecutive 3
# Leetcode 1004
'''
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

Example 1:
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Example 2:
Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
'''

# Brute Force Solution     TC -> o(n^2)   SC -> o(1)

class Solution:
    def longestOnes(self, nums, k):
        max_length = 0
        n = len(nums)
        for i in range(n):
            zeros = 0
            for j in range(i, n):
                if nums[j] == 0:
                    zeros += 1
                if zeros <= k:
                    length = j - i + 1
                    max_length = max(max_length, length)
                else:
                    break
        return max_length
sol = Solution()
print(sol.longestOnes(nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3))


# Better Solution       TC - o(2N)    SC -> o(1)
# Using Sliding window with shrink loop

class Solution:
    def longestOnes(self, nums, k):
        max_length = 0
        left = 0
        right = 0
        zeros = 0
        n = len(nums)
        while right < n:
            if nums[right] == 0:
                zeros += 1
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            if zeros <= k:
                length = right - left + 1
                max_length = max(max_length, length)
            right += 1
        return max_length
sol = Solution()
print(sol.longestOnes(nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3))


# Optimal Solution      TC -> o(N)   SC -> o(1)

class Solution:
    def longestOnes(self, nums, k):
        left = 0
        right = 0
        n = len(nums)
        zeros = 0
        max_length = 0
        while right < n:
            if nums[right] == 0:
                zeros += 1
            # The only diff between better and optimal Ssolution, we are using if instead of while
            if zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            if zeros <= k:
                length = right - left + 1
                max_length = max(max_length, length)
            right += 1
        return max_length

sol = Solution()
print(sol.longestOnes(nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2))