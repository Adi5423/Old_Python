import time 
star = ' '
ind = 0
sat = str(input("Enter a word upto 6 Albhabets!! = "))
sat2 = len(sat)

for i in range(97,97+sat2):

    time.sleep(.500)

    print(star,chr(i) , '\n')
    if( chr(i) == chr(ind)):
        #print(chr(i).upper() , '\n')
        star += chr(i).upper()
        i = 97 
        pass
    else:
        continue