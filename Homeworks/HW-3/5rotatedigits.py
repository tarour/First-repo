def rotate_digits():
    n = input('Input the integer you want to rotate: ')
    number_of_digits = 0
    x = int(n)
    while x != 0:
        x = x // 10
        number_of_digits += 1
    
    x = int(n)  # this is to set x = n again after the while loop

# keep on floor dividing the number to get the number of digits
# after getting the number of digits, we can rotate the number
# normally i'd just cast the input to a string and take len() to get the number of digits but we can't do that here

    new_n = (x // 10) + (x % 10)*(10**(number_of_digits - 1))
    return print(new_n)

# checking to make sure the function works
rotate_digits()



