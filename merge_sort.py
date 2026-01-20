nums = [2,4,2,5,92,2,38,483,9,24,2,9,4,8,2,3,5,3]

# performing merging here

def merge(left, right):
    n = len(left)
    m = len(right)
    i = j = 0
    result = []
    
    while i < n and j < m:
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# now perfoming merge sort

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

print(merge_sort(nums))