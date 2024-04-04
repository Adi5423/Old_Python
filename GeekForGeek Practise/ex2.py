'''
Given a list in Python and provided the positions of the elements, write a program to swap the two elements in the list. 

Examples:  

Input : List = [23, 65, 19, 90], pos1 = 1, pos2 = 3
Output : [19, 65, 23, 90]

Input : List = [1, 2, 3, 4, 5], pos1 = 2, pos2 = 5
Output : [1, 5, 3, 4, 2]
'''


l = [ 23, 65,29 , 90]
po1 = int(input("Enter q number"))
po2 = int(input("Enter a number"))
print(l)
l[po1-1] = l[po2-1]
print(l)