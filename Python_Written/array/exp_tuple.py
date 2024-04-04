ind = int(input("Enter the Length of the Tuple!! = ")) #range entered by the user 
t = tuple() #empty tuple created 
for i in range (ind):
    ar = input("Enter a Element: = ") #taking the values 
    t += (ar ,) #empty tuple will input a value as ar_var last comma will represent it's tuple.
print(type(t))
print(t)