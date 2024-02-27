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

# I made two errors here. The first is that I forgot to put quotation marks around the question mark. Because of this, the question mark was not classified as a string, and therefore was not able to be added to modify the list.

# The second mistake was that I wrote the index of the jth index of the ith index of the 2D array wrong (namely fivebyfive[i[j]]). To be honest I did not fully think this code through when I first wrote it, so the issue became rather obvious when I stared at it for a few seconds. But it is an error I made nonetheless, so I am obligated to document it.

print(fivebyfive)


