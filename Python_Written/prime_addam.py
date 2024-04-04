m = int(input("Enter a Number"))
n = int(input("Enter another Number"))
a = m+1
rev = 0
c = a
end = " "
if n>0 and m>0:
    if(m<n):
        if(a>m and a<n or c>m and c<n):
            if(a%a == 0 and a%1 == 0):
            #Cube of the number between m and n
                cube= a**2
            
            #Reverse of the number 
                b = a
                while a > 0:
                    dig = b%10 
                    rev = rev*10+dig
                    a //=10


            #Cube of Revrese of the Number
                cube_2 = rev**2
            #Reverse of reversed number cube(revresing the cube)
                rev_2 = 0 
            #Reverse of cube of the reversed numbere(revresing the cube)             
                cb = cube_2
                while cb>0:
                    dig_2 = cube_2%10
                    rev_2 = rev_2*10+dig_2
                    cb //= 10
                if(cube == rev_2):
                    print("The numbers between " + m + 'and ' + n + 'are =' + c + end)
        a +=1


'''Reverse the Number 
num2 = num #the orignal number
while num2 > 0 :
    dig = num % 10     
    rev = rev*10+dig
    num //= 10''' 