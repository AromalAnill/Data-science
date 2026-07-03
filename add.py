dividend = float(input("Enter the dividend: "))
divisor = float(input("Enter the divisor: "))

if divisor == 0:
    print("Error: Division by zero is not allowed.")
else:
    result = dividend / divisor
    print("Result =", result)