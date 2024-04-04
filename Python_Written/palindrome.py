num = int(input("Enter a Number"))

rev = 0 

num2 = num
while num2 > 0 :
    dig = num % 10
#it will remove the rightmost portion of the number ex. (313%10 = 3)
#we use dthe 10 number here cause we just want a single number from the rightmost portion.
    rev = rev*10+dig
#rev was intialised as 0 first so we multiplied it by 10 and rev will be updated as 3 because of the addition of dig 3.
#then the next line will be excuted and the num will be 31 and 1 will be in dig , in rev 3 was stored it will be multiplied by 10 = 30 and then will be added by 1(dig) = 31 , later will be converted to 313.
    num2 //= 10 
#num2 = num2//10 (it will remove a single digit(rightmost) from the last of digit ex. [313 // 10 = 31]) the loop will be executed till it becomes 0

if num == rev :
    print("It's Palindrome")
else:
    print("Not Palindrome")