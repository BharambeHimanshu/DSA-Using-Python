# Lower and Upper Bound

# Lower Bound [smallest index such that nums[i]>= target]   TC -> o(log2n)    SC -> o(1)

nums = [1,1,2,3,4,5,6,6,7,8,9]
target = 2

def lowerbound(nums,target):
    n = len(nums)
    low = 0
    high = n-1
    lb = n
    while low <= high:
        mid = (low+high) // 2
        if nums[mid] >= target:
            lb = mid
            high = mid - 1
        
        else:
            low = mid + 1
    return lb

print(lowerbound(nums,target))


# Upper Bound   [smallest index such that nums[i]> target]   TC -> o(log2n)    SC -> o(1)
nums = [1,1,2,3,4,5,6,6,7,8,9]
target = 2

def lowerbound(nums,target):
    n = len(nums)
    low = 0
    high = n-1
    ub = n
    while low <= high:
        mid = (low+high) // 2
        if nums[mid] > target:
            ub = mid
            high = mid - 1
        
        else:
            low = mid + 1
    return ub

print(lowerbound(nums,target))