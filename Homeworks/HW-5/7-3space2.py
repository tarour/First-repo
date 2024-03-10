import numpy as np

myarr = np.array(['python','is','cool'])


def spaceBetween(arr):
    arr2 = np.empty_like(arr)

    stringlist = []
    
    for i in range(len(arr)): 
        
        x = ' '.join(arr[i])
        
        stringlist.append(x)
    
    stringarr = np.array(stringlist)

    return stringarr


print(spaceBetween(myarr))







