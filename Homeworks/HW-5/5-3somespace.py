
# This code doesn't work; I just want to keep this file here as proof of my effort.



import numpy as np

myarr = np.array(['python','is','cool'])


def spaceBetween(arr):
    
    arr2 = np.empty_like(arr)

    stringlist = []
    
    print(arr2)

    for i in range(len(arr)): 
        
        x = ' '.join(arr[i])
        
        print(x,arr2[i])
        
        arr2[i] = x
        
        print(arr2[i])

    return arr2


print(spaceBetween(myarr))







