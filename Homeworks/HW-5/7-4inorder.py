import numpy as np

np.random.seed(12345)
a = np.random.randint(1,50,(4,5))

print(a)

def sorting(arr):
    
    arr2 = np.sort(arr,axis = 0)
    
    return arr2

print(sorting(a))

# An easier way to do this is to just sort the array directly.

print(np.sort(a,axis = 0))




