num1 = (input("Enter first number:"))    # this is where you input the numbers
op = (input("Enter operator:"))          # this is where you input the operator
num2 = (input("Enter second number:"))   # this is where you input the numbers

 # if and else statements for what op you choose
if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
elif op == "//":
    print(num1 // num2)    
else:
    print("invalid operator")                   
