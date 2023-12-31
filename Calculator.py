def add(num1, num2):
  return num1 + num2

def subtract(num1, num2):
  return num1 - num2

def multiply(num1, num2):
  return num1 * num2

def divide(num1, num2):
  return num1 / num2

def calculate():
  num1 = float(input("Enter the first number: "))
  num2 = float(input("Enter the second number: "))

  operator = input("Enter the operator (+, -, *, /): ")

  if operator == "+":
    result = add(num1, num2)
  elif operator == "-":
    result = subtract(num1, num2)
  elif operator == "*":
    result = multiply(num1, num2)
  elif operator == "/":
    result = divide(num1, num2)
  else:
    print("Invalid operator.")
    return

  print(f"{num1} {operator} {num2} = {result}")

if __name__ == "__main__":
  calculate()
