# Longest Consecutive Sequence
# Leetcode 128

# Brute Force

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