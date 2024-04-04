n = int(input("Enter a No."))

#intialize Sum 
sum = 0 

# find the sum and cube of the number 
temp = n 
while temp > 0 :
    digit = temp % 10  
#it will remove the rightmost portion of the number ex. (153%10 = 3)
#we use dthe 10 number here cause we just want a single number from the rightmost portion.
#if we will use 100 instead 10 it will take two number from the rightmost of it ex 53 will be the oupt of 153. 
    sum += digit ** 3 
#the cube will be added to the sum of cubed numbers
    temp //= 10 
#temp = temp//10 (it will remove a single digit(rightmost) from the last of digit ex. [153 // 10 = 15]) the loop will be executed till it becomes 0

if n == sum:
    print("Armstrong")
else :
    print("Not Armstrong")