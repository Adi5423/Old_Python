ar = int(input("ENter a Number"))
sum = 0 
av = ar
aa = av
while aa >0:
    dig = ar%10
    sum += dig**3
    aa //= 10
if(sum == av):
    print('Armstrong')
else:
    print('Not Armstrong')