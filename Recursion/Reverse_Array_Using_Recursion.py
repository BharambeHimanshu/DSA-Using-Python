# Reverse Array Using Recursion

nums = [5,9,8,7,6,5,4,7,4]

def func(nums,left,right):
    if left >= right:
        return
    nums[left], nums[right] = nums[right], nums[left]
    func(nums,left+1,right-1) 

# func(nums,2,6) #Select particulur arr
func(nums,0,len(nums)-1) # Selecting entire

print(nums)