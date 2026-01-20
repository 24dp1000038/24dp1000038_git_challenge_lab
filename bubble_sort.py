# implementing bubble sort

import random
nums = [i for i in range(5,57,2)]
random.shuffle(nums)

# time complexity O(n^2) 
def bubble(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr

print(bubble(nums))
