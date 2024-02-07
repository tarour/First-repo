def digroot():
    
    integer = int(input('Input the integer you want the digital root of: '))
    string = str(integer)
    digital_root = 0 # this will be the sum we add to in our for loop
    for i in range(0,len(string)):
        digital_root += int(string[i])
    
    return print(digital_root)

digroot()


