num1 = (input("Enter first number:"))
op = (input("Enter operator:"))
num2 = (input("Enter second number:"))
# if and else statements for what op you choose
if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("invalid operator")                   
