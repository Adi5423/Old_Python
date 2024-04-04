str = input("Enter to search ")
ch = input("Enter the Line")
count = 0 
for char in ch:
    if char == str:
        count +=1
print("The word is repeatin in the line=" , count , 'times') 