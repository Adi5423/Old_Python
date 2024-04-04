sr = ' '
r = input("Press \'A\' for execution!!")
id = 97
if r =='a' or r =='A':
    while sr != 'hacker' or sr != 'HACKER':
        print(chr(id) , '\n')
        if(chr(id) == 'h'):
            sr += chr(id) 
            print(sr.upper())
        elif(chr(id) == 'a'):
            sr += chr(id) 
            print(sr.upper())
        elif chr(id) == 'c':
            sr += chr(id) 
            print(sr.upper())
        elif chr(id) == 'k':
            sr += chr(id) 
            print(sr.upper())
        elif chr(id) == 'e':
            sr += chr(id) 
            print(sr.upper())
        elif chr(id) == 'r':
            sr += chr(id) 
            print(sr.upper())
        else:
            id +=1