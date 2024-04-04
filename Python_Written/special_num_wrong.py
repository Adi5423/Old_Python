num = int(input("Enter a number"))

result = 1

temp = num
while temp>0:
    dig = temp%10
    factor =dig
    while factor >0 :
        result *= factor
        factor -= 1
        temp //=10
if(result == num ):
    print("Special Number")