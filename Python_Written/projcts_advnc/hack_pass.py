from random import *
import os 
upd = input("Enter the password!! = ")
pwd = ['a', 'b ' , 'c' , 'd' ,'e','f' , 'g' , 'h' , 'i', 'j' , 'k' , 'l', 'm' , 'n' ,'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' , '1', '2' , '3' , '4' , '5' ,'6' , '7','8','9']

pw = ""
while(pw!=upd):
    pw =''
    for letter in range(len(upd)):
        guess = pwd[randint(0,17)]
        pw = str(guess) + str(pw)
        print(pw)
        print("Cracking PAssword....Please wait!!")
        os.system("cls")
print("Your password Is :" , pw)