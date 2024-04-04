num = int(input("Enter the Number = "))
st = ''
q1 = 1
i = 0
while(q1 != 0): 
    q1 = num//2
    r1 = num%2
    st += str(r1)
    q2 = q1//2
    r2 = r1%2
    st += str(r2)
le = len(st)    
for i in range(le):    
    st2 = st[-le]
    le -=1
print(st2)