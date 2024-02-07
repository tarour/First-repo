def vowelnum():
    word = input('Input the word(s) you want to count the vowels of: ')
    string = str(word)
    count = 0 # this is our vowel count

    for i in range(0,len(string)):
        if string[i] == 'a' or string[i] == 'A' or string[i] == 'e' or string[i] == 'E' or string[i] == 'i' or string[i] == 'I' or string[i] == 'o' or string[i] == 'O' or string[i] == 'u' or string[i] == 'U':
            
            count += 1
    
    # add 1 to count every time the loop encounters a vowel

    if count == 1:
        return(print('There is 1 vowel in', string))

    else:
        return(print('There are', count, 'vowels in', string))

vowelnum()

