# Floor and ceil
# Floor - largest no. of array <=target
# Ceil - smallest no> of array >=target

nums = [3, 4, 4, 4, 8, 9, 9,10, 12, 12, 14, 15]
target = 6

def floorandceil(nums,target):
    n = len(nums)
    ceil = -1  #Taking -1 beacuse if value not present in array it will return -1
    floor = -1
    low = 0
    high = n - 1
    while low <= high:
        mid = (low+high) // 2
        if nums[mid] == target:
            return [nums[mid],nums[mid]]
        elif nums[mid] > target:
            ceil = nums[mid]
            high = mid -1
        else:
            floor = nums[mid]
            low = mid + 1
        
    return [floor,ceil]

print(floorandceil(nums,target))