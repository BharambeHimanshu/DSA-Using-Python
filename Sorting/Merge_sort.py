#Merge sort

# For two sorted array

left = [1,2,3,4]
right = [1,1,3,4,5,6,7]

def merge_array(left,right):
    result = []
    i,j = 0,0
    n,m = len(left), len(right)
    while i < n and j < m:
        if left[i] <= right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1


# Copy the elements of left,if any

    while i < n:
        result.append(left[i])
        i+=1
        
# Copy the elements of right,if any

    while j < m:
        result.append(right[j])
        j+=1
    return result

print(merge_array(left,right))

# Merge sort 

nums = [3, 1, 2, 4, 1, 5, 2, 6, 4]
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2  # Correct the integer division
    left_arr = arr[:mid]
    right_arr = arr[mid:]
    left = merge_sort(left_arr)
    right = merge_sort(right_arr)
    return merge_array(left, right)


print(merge_sort(nums))
