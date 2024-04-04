#Ouestion 3
#Calculate the BMI(Body Mass Index) using the formula = (weight/height^2) by taking th Values from the user.

#sol.
print("Hello User!")
print("Let's calculate the BMI(Body Mass Index)")
wei = input("Enter the Weight of the Body")
hei = input("Enter the Height of the Body")
hei = int(hei)
wei = int(wei)
hei_2 = hei**2
bmi = (wei/hei_2)
bmi_2 = (wei//hei_2)
print("The BMI of the body is =" + str(bmi) + " " + "or" + " " + str(bmi_2))