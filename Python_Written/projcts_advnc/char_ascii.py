import time 
# A-Z = 65 - 90 
# a-b = 97 - 122
# ord() to get the ascii code 
# chr() to convert the ascii into alphabet
str = ' '
h = 97 #8
a = 97 
c = 97 
k = 97  #11 
e = 97  #5
r = 97  #18
while(r < 115):
    #for i in range(0, 24 , 1):
        print(chr(h),chr(a),chr(c) , chr(k) , chr(e) , chr(r) , end = " \n")
        time.sleep(.500)
        if( h == 104 ):
           #if(h ==72 ):
           #    pass
           #    print(h, 'e')
           #elif h < 105 and h>96:
           #     h += 1
           #     print(h, 'r')
           #elif h!= 72:
           #    h = 72
           #    print(h, 't')
            pass
        else:
            #if h < 105 and h>96:
            h += 1
                #print(h, 'r')
        if(a == 97 ):
            #if chr(a) == 'a':
             #   a -= 32 
            pass
        else:
            #if(a <=65 ):
            #    pass
#            elif a < 98:
                 a += 1
#            else:
#               a = 65
            
        if( c == 99):
            pass     
        else:
            c += 1
        if(k == 107 ):
            pass
        else:
            k += 1
        if(e == 101):
            pass
        else:
            e += 1
        if(r == 97+17 ):
            pass
        else:
            pass
        r += 1
#print(str.upper())
#print(chr(h).upper(),chr(a).upper(),chr(c).upper() , chr(k).upper() , chr(e).upper() , chr(r-1).upper() , end = " \n")
#print(chr(97+17))