# Merge two sorted array without duplicates

nums1 = [1, 1, 1, 2, 4, 6, 7]
nums2 = [1, 2, 3, 6, 7, 8, 9, 10]

def sortedarray(nums1, nums2):
    i = 0
    j = 0
    result = []

    while i < len(nums1) and j < len(nums2):
        if nums1[i] != nums2[j]:
            if len(result) == 0 or result[-1] != nums1[i]:  # Result[-1] used to check the last number of result
                result.append(nums1[i])
            i+=1
        else:
            if len(result) == 0 or result[-1] != nums2[j]:  
                result.append(nums2[j])
            j+=1
    
    while i < len(nums1):
        if len(result) == 0 or result[-1] != nums1[i]:  
            result.append(nums1[i])
        i+=1

    while j < len(nums2):
        if len(result) == 0 or result[-1] != nums2[j]:  
            result.append(nums2[j])
        j+=1

    return result

print(sortedarray(nums1, nums2))
