nums = [2,4,2,5,92,2,38,483,9,24,2,9,4,8,2,3,5,3]

def insertion(arr):
    n = len(arr)
    
    for i in range(1,n):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        
        arr[j+1] = key
    return arr

print(insertion(nums))
            