# Given a list, write a Python program to swap first and last element of the list.

# Approach #1: Find the length of the list and simply swap the first element with (n-1)th element.

l = [342,425,24,225,324,3,241,4123,323]

print(l[0] , l[len(l)-1])

def swap (l):
    last = len(l)
    l[0] = l[last-1] 
    print(l[0] , l[(len(l)-1)])
    
swap(l)