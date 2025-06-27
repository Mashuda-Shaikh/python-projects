no1=float(input("Enter First Number: "))
no2=float(input("Enter Second Number: "))
operation=input("Choose any one operation e.g.(+, -, *, / ): ")

if operation=='+':
    print("The Addition is ", (no1+no2))

elif operation=='-':
    print("The Subtraction  is ", (no1-no2))

elif operation=='*':
    print("The Multiplication is " , (no1*no2))

elif operation=='/':
    if no2==0:
       print("Error: Division by zero is not allowed.")
    else:
        print("The Division  is ", (no1/no2))

else:
    print("Invalid Operation")
