# this is the main file in the main branch

# performing some kind of sorting algorithm here

# Inbuild sorting

import random
nums = [i for i in range(5,57,2)]
random.shuffle(nums)

print(f"This is arr before sorting :- {nums}")
arr = sorted(nums)

print(f"After time sort or builtin sort :- {arr}")