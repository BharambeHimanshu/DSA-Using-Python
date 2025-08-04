# Longest Consecutive Sequence
# Leetcode 128
'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Example 3:
Input: nums = [1,0,1,2]
Output: 3
'''

# Brute Force  TC -> o(N^2)   SC -> o(1)

nums = [1, 99, 101, 98, 2, 5, 3, 100]

def Sequence(nums):
    n = len(nums)
    max_count = 0
    for i in range(0,n):
        num = nums[i]
        count = 1
        while num + 1 in nums:
            count += 1
            num = num + 1
    max_count = max(max_count,count)
    return max_count

print(Sequence(nums))


# Better Solution  TC -> o(NNlogn + N)     SC -> o(1)

nums = [0,3,7,2,5,8,4,6,0,1]

def longestConsecutive(nums):
    nums.sort() # Sort array
    count = 0
    last_smaller = float("-inf")
    longest = 0
    for i in range(0,len(nums)):
        num = nums[i]
        if num - 1 == last_smaller:
            count += 1
            last_smaller = num
        elif num != last_smaller:
            count = 1
            last_smaller = num
        longest = max(longest,count)
    return longest

print(longestConsecutive(nums))


# Optimal Solution using sets  TC -> o(N)   SC -> o(N)

nums = [100,4,200,1,3,2]

def Longestconsecutive(nums):
    my_set = set()
    for i in range(0,len(nums)):
        my_set.add(nums[i])
    longest = 0
    for num in my_set:
        if num - 1 not in my_set:
            x = num
            count = 1
            while x+1 in my_set:
                count += 1
                x += 1
            longest = max(longest,count)
    return longest

print(Longestconsecutive(nums))