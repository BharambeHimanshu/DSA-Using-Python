# Bubble Sort [Adjacent Elements]

nums = [4,6,3,8,9,10,2]

n = len(nums)
for i in range(n-2,-1,-1):
    for j in range(0,i+1):
        if nums[j] > nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]

print(nums)