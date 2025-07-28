# Find the second largest element in an array

#Brute Force Solution TC -> o(n logn) SC -> o(1)

nums = [55,32,97,-55,45,32,88,21]
n = len(nums)
nums.sort()
print("The second Largest element is: ",nums[n-2])

#Better Solution TC -> o(n*n) SC -> o(1)

nums = [55,32,97,-55,45,32,88,21]
largest = float("-inf")
second_largest = float("-inf")
n = len(nums)
for i in range(0,n):
    largest = max(largest,nums[i])
for i in range(0,n):
    if nums[i] > second_largest and nums[i] != largest:
        second_largest = nums[i]
        
print("The second largest element is: ",second_largest)


#Optimal Solution TC -> o(n)  SC -> o(1)
nums = [55,32,97,-55,45,32,88,21]
largest = float("-inf")
second_largest = float("-inf")
n = len(nums)
for i in range(0,n):
    if nums[i] > largest:
        second_largest = largest
        largest = nums[i]
    elif  nums[i] > second_largest and nums[i] != largest:
        second_largest = nums[i]
            
print("The second largest element is: ",second_largest)