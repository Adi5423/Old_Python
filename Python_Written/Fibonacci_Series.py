n = int(input("Enter a Number"))

'''for i in range(0 , n==0 ):
        fs = (n-1) + (n-2)
        print(fs , end= " ")
#Sum of all the number before the inputed int
# ( ex - N = 10 , the output = 0,1,1,2,3,5,8,13,21,34)''' 
sum = 0 

a=0
b=1
while a<n:
    a = b 
    b = sum 
    sum = a+ b
    print(sum , end = " ")