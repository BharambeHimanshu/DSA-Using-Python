# Remove Duplicates From Sorted Array 
# Leetcode Problem 26

# Brute Force  TC-> o(2n)  SC -> o(n)


def remove_duplicates(nums):
    n = len(nums)
    freq_map = {}
    for i in range(n):
        freq_map[nums[i]] = 0
        
    j = 0
    for k in freq_map:
        nums[j] = k
        j += 1
    return j

nums = [1,1,1,2,3,4,4,7,9,9,9,10]
result = remove_duplicates(nums)
print(result)
print(nums[:result])


# Optimal Solution  TC -> o(n)     SC -> o(1)


def removeDuplicates(nums):
    if len(nums) == 1:
        return 1
    i = 0
    j = i + 1
    while j < len(nums):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
        j += 1
    return i + 1

# Example usage
nums = [1,1,1,2,3,4,4,7,9,9,9,10]
result = removeDuplicates(nums)
print(result)
print(nums[:result])

