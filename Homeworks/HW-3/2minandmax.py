def minmax(x):
    xmin = min(x)
    xmax = max(x)
    return (xmin,xmax)

# checking to ensure that the function works as intended
print(minmax([3,6,1,2,45]))
print(type(minmax([3,6,1,2,45])))
