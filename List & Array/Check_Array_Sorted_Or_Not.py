# Check if the array list is sorted or not

# Optimal Solution TC -> O(n)  SC -> O(1)

nums = [3, 5, 6, 8, 9, 10, 23]
def is_sorted(nums):
    n = len(nums)
    for i in range(n - 1):
        if nums[i] > nums[i + 1]:
            return False
    return True

print(is_sorted(nums))