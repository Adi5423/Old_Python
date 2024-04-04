'''ar = str(input("Enter a KeyWord"))
ae = str(input("Enter a KeyWord to be searched"))
l1 = ["Hello" , 34 , "The Argument you entered above" , ae in ar , ]
print(l1)'''

l1 =[ 'HEllow' , 32 , 'Sharks' , True , "Error!!"]
print(l1)
for i in l1:
    if(type(i) == str):
        print("Executing!! \n") 
        print(i) 
        print("THe variable data type is a String \n")
        if('a' in i ):
            i.replace('a' ," ")
        elif('e' in i ):
            i.replace('e' ," ")
        elif('i' in i ):
            i.replace('i' ," ")
        elif('o' in i ):
            i.replace('o' ," ")
        elif('u' in i ):
            i.replace('u' ," ")
    else:
        print("Error!!")
print(l1)
'''elif(type(i) == int):
        print('Executing!! \n')
        print(i)
        print("The variable seems as a Integer Data Type \n")
    elif(type(i) == bool):
        print("Executing!! \n")
        print(i)
        print("Looks like a couple \'Joined the Chat\' Data Type Boolean \n")
    else:
        print("Rerun the software/program!! \n")
        print("The list is = " , l1 )'''