def minimaxi(number_list):
    x = number_list[0]  # initially setting the min and max to the first item on the list
    y = number_list[0]
    for i in range(1,len(number_list)):
        if number_list[i] > x:
            x = number_list[i]
        if number_list[i] < y:
            y = number_list[i]

    minmax = (y,x)
    return minmax

# checking that the function works

print(minimaxi([3, 6, 1, 5, 8]))
print(type(minimaxi([3,6,1,5,8])))
