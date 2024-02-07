def nmbrpwr():
    x = input('Input a number: ')
    y = input('Input the power you want to raise it to: ')
    t = 1

# writing a for loop that multiplies x by itself y number of times
    for i in range(0,int(y)):
        t *= int(x)
    return print(t)

nmbrpwr()
