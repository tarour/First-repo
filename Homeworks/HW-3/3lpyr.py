def leapyr():
    yr = input('Input a year: ')
    year = int(yr)
    
    if year%400 == 0:
        return print(True)

    elif year%100 == 0:
        return print(False)

    elif year%4 == 0:
        return print(True)
    
    else:
        return print(False)
leapyr()
