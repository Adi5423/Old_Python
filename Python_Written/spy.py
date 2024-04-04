n = int(input("Enter a Number"))

sum = 0
pro = 1

temp = n
while temp>0:
    dig = temp%10
    sum += dig
    temp //= 10

temp = n
while temp>0:
    dig = temp%10
    pro *= dig
    temp //= 10

if(sum == pro):
    print("It's a spy number")
else:
    print("It's not a spy number")