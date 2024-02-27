# Part 1

Numbers0to50 = [x for x in range(0,51)]


# Part 2

def SquaredList(inputlist):

    return [y**2 for y in inputlist]

# Check to ensure the function works
print(SquaredList(Numbers0to50))


# Part 3

listA = [x for x in range(1,11)]
listB = [y for y in range(20,31)]
print(listA, listB)

def Oddlist(A,B):
    C = A + B
    return [x for x in C if x%2 == 1]

print(Oddlist(listA,listB))




