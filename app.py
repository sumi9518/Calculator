print("Simple Calculator")

try:
    num1 = float(input("Enter the first number : "))
    operator = input("Enter the operator (+,-,*,/) : ")
    num2 = float(input("Enter the second number : "))

    if operator == "+":
        print(num1+num2)

    elif operator == "-":
        print(num1-num2)

    elif operator == "*":
        print(num1*num2)

    elif operator == "/" :
        if num2 == 0:
            print("Cannot divide by 0")
        else:
            print(num1/num2)
    else:
        print("Invalid Operator")

except ValueError:
    print("Please enter a valid number")