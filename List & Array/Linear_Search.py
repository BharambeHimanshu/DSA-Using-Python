# Linear Search in Python
# 3 Rules
# 1st -> return a index of target value if there are no duplicates 
# 2nd -> return the 1st occuring index of target value if there are duplicates values in list
# 3rd -> no match return -1

# TC -> o(n)
# SC -> o(1)

nums = [4,5,3,2,7,8,5,4,1]
target = 4 
def linearSearch(nums, target):
    for i in range(0,len(nums)):
        if nums[i] == target:
            return i
    return -1

print(linearSearch(nums, target))