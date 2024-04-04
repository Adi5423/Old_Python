#WAP to change any string in the list to the string provided by the user!!
import time 
l = ["ar" , "re" , "erer" , "adi" , "Hellow World!!" , "World Hellow!!"]
r = 0 
print(len(l) , "The Length of the" , type(l) , "\n")
for i in l:
    #print(len(l) , "The Length of the" , type(l))
    a = l[r]
    print(r+1 , "=" , a)
    r += 1 
we = input("It incl. the ingredient you need??")
if we == 'y':
    te = str(input("Enter the String to be replaced!! = "))
    print("Processing!!\n")
    ind = l.index(te)
    #rem = l[ind]
    l.remove(l[ind])
    time.sleep(.500)
    wer = str(input("Enter the String to be inputed instead!! = "))
    print("Processing Again!!\n")
    l.insert(ind , wer)
    time.sleep(2)
    r = 0
    for j in l:
        #print(len(l) , "The Length of the" , type(l))
        a = l[r]
        print(r+1 , "=" , a)
        r += 1 