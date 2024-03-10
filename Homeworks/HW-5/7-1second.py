import numpy as np

arr = np.array([[1,1,1],[1,2,3],[2,2,2]])

def findEqual(arr):
    
    arr2 = arr

    for i in range(len(arr)):
        #print(len(np.unique(arr[i])),arr[i])
        if len(np.unique(arr[i])) != 1:
            arr2 = np.delete(arr,i,0)

    return arr2

print(findEqual(arr))






