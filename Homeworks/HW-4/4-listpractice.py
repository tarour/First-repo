
def removeDuplicates(lis): 

    for i in range(0,len(lis)):
        if i == len(lis):
            break
    # This block stops the for loop if i exceeds the list index count; this occurs because we continually remove values from the list, and so len(lis) continually decreases.

        while lis.count(lis[i]) > 1:
            lis.remove(lis[i])
            
    return lis

print(removeDuplicates([1,1,2,3,4,4]))





