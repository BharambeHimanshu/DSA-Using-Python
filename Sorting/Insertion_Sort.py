# Insertion Sort [Compare previous element]

nums = [3,5,7,2,4,10,8,9]

n = len(nums)
for i in range(1,n):
    key = nums[i] # To the the value which is less than the 
    j = i - 1 # To assign the previous value
    while j>=0 and nums[j]>key:
        nums[j+1] = nums[j]
        j-=1
    nums[j+1] = key
    
print(nums)