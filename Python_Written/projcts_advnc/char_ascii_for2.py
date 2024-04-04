import time 
star = ' '
#sat = str(input("Enter a word of "))
for i in range(97,115):
    time.sleep(.500)
    print(star,chr(i) , '\n')
    if( chr(i) == 'h'):
        #print(chr(i).upper() , '\n')
        star += chr(i).upper()
        i = 97 
        pass
        if( chr(i) == 'a'):
            #print(chr(i).upper() , '\n')
            star += chr(i).upper()
            i = 97
            pass
            if( chr(i) == 'c'):
                #print(chr(i).upper() , '\n')
                star += chr(i).upper()
                i = 97
                pass
                if( chr(i) == 'k'):
                    #print(chr(i).upper() , '\n')
                    star += chr(i).upper()
                    i = 97 
                    pass
                    if( chr(i) == 'e'):
                        #print(chr(i).upper() , '\n')
                        star += chr(i).upper()
                        i = 97
                        pass
                        if( chr(i) == 'r'):
                            #print(chr(i).upper() , '\n')
                            star += chr(i).upper()
                            i += 32
                            pass
if( star == 'HACKE r'):
    print(star.upper())
else:
    pass   