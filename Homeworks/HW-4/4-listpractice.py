
def removeDuplicates(lis): 

    for i in range(0,len(lis)):
        if i == len(lis):
            break
    # This block stops the for loop if i exceeds the list index count; this occurs because we continually remove values from the list, and so len(lis) continually decreases.

        while lis.count(lis[i]) > 1:
            lis.remove(lis[i])
            
    return lis

# This part of the assignment is by far the one I made the most errors in. Namely, I encountered an indexing error in the while loop. This occurred because i ranges from 0 to len(lis), but the len(lis) value does not update even if I remove elements from lis. It took me an embarrasingly long time to write the if statement breaking the loop once it surpasses the index range; since the i == len(lis) statement occurs in the for loop, the len(lis) value is updated for each iteration, so we can use it to reliably end the loop.


print(removeDuplicates([1,1,2,3,4,4]))





