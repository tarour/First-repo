# Note - this file does indeed solve the problem for 7.1 - but I wrote a second file for this problem as its solution is much more simple than this one.
# I simply preferred to submit this file as proof of my effort.


import numpy as np


arr = np.array([[1,1,1],[1,2,3],[2,2,2]])


def findEqual(arr):

    equalarr = np.array([])
    i = 0
    
    for row in arr:
        
        if len(row) == list(row).count(row[0]):
            i += 1
            equalarr = np.append(equalarr,[row])
    
    eqarr = equalarr.reshape(i,len(arr[0]))

    print(eqarr.ndim)
    return eqarr


print(findEqual(arr))




