# Move Zeros to end 
# Leetcode 283
'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
'''

# Brute Force Solution   TC -> o(2n)   SC -> o(n)
nums = [1, 0, 2, 4, 3, 0, 0, 3, 5, 1]
def MoveZeros(nums):
    n = len(nums)
    temp = []

    # Copy non-zero elements from original to temp array
    for i in range(0,n):
        if nums[i] != 0:
            temp.append(nums[i])

    # Number of non-zero elements
    nz = len(temp)

    # Copy elements from temp to fill first nz fields of original array
    for i in range(0,nz):
        nums[i] = temp[i]

    #Fill the rest of the cells with 0
    for i in range(nz,n):
        nums[i] = 0
    return nums

print(MoveZeros(nums))


# Optimal Solution (Without Using Temp Variable) TC -> o(n)   SC -> o(1)

nums = [1, 0, 2, 4, 3, 0, 0, 3, 5, 1]
def MoveZero(nums):
    if len(nums) == 1:
        return
    i = 0
    while i < len(nums):
        if nums[i] == 0:
            break
        i += 1
    else:
        return
    j = i + 1
    while j < len(nums):
        if nums[j] != 0:
            nums[i],nums[j] = nums[j],nums[i]
            i += 1
        j +=1
    return nums

print(MoveZero(nums))
