# implementin selection sort here

def selection(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        
    return arr

nums = [2,4,2,5,92,2,38,483,9,24,2,9,4,8,2,3,5,3]

print(selection(nums))
