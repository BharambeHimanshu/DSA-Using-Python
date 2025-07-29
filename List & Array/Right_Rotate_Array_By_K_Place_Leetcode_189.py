# Right rotate array by k Place
# Leetcode Problem 189 (Med)

# Brute Force Solution  TC -> o(r*n)   SC -> o(1)

def rotate(nums, k):
    n = len(nums)
    rotations = k % n  # in case k > n
    for _ in range(rotations):
        last = nums.pop()
        nums.insert(0, last)
    # Function modifies nums in-place

# Example usage:
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
rotate(nums, k)
print(nums) 



# Better Solution Using Slicing
def rotate(nums,k):
    n = len(nums)
    k %= n

    # Rotate the list in-place
    nums[:] = nums[n - k :] + nums[: n - k]

# Example usage:
nums = [1, 2, 3, 4, 5, 6, 7,8,9,10]
k = 3
rotate(nums, k)
print(nums) 



#Optimal Solution Without Using Slicing
# Here we make using of the concept of reverse array

def reverse(nums, left, right):
        # Reverse nums[left:right+1] in-place
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

def rotate(nums, k):
    n = len(nums)
    k = k % n
    # 1. Reverse last k elements
    reverse(nums, n - k, n - 1)
    # 2. Reverse first n - k elements
    reverse(nums, 0, n - k - 1)
    # 3. Reverse the entire array
    reverse(nums, 0, n - 1)

# Example usage
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
k = 3
rotate(nums, k)
print(nums) 