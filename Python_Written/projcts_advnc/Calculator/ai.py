def add(num1, num2):
  return num1 + num2

def subtract(num1, num2):
  return num1 - num2

def multiply(num1, num2):
  return num1 * num2

def divide(num1, num2):
  return num1 / num2

def calculate():
  # Prompt the user for two numbers.
  num1 = float(input("Enter the first number: "))
  num2 = float(input("Enter the second number: "))

  # Prompt the user for an operation.
  operation = input("Enter an operation (+, -, *, /): ")

  # Perform the operation and print the result.
  if operation == "+":
    result = add(num1, num2)
  elif operation == "-":
    result = subtract(num1, num2)
  elif operation == "*":
    result = multiply(num1, num2)
  elif operation == "/":
    result = divide(num1, num2)
  else:
    print("Invalid operation.")
    return

  print(f"{num1} {operation} {num2} = {result}")

# Calculate until the user quits.
while True:
  calculate()

  # Ask the user if they want to calculate again.
  again = input("Do you want to calculate again? (y/n): ")

  if again != "y":
    break
