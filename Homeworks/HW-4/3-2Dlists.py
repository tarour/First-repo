# Part 1

fivebyfive = []

for i in range(0,5):
    
    rowlist = []

    for j in range(1,6):
    
        rowlist.append(5*i + j)

    fivebyfive.append(rowlist)

print(fivebyfive)


# Part 2

for i in range(0,5):


    for j in range(0,5):
        
        if fivebyfive[i][j] % 3 == 0:
            fivebyfive[i][j] = '?'

print(fivebyfive)


