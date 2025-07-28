# Find the largest element in an array

#Using Inbuilt function max
nums = [55,32,-97,99,3,67]
largest = nums[0] # output : 55
n = len(nums)
for i in range(0,n):
    largest = max(largest,nums[i]) # max(55,32)

print("The largest element is: ", largest)

#Using IF-else
nums = [55,32,-97,99,3,67]
largest = nums[0] # output : 55
n = len(nums)
for i in range(0,n):
    if nums[i] > largest:
        largest = nums[i]
print("The largest element is: ", largest)

