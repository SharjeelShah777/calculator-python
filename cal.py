operators = input("Enter Your Operators  (+ - / * // **): ")
num1 = float(input("Enter your 1st number: "))
num2 = float(input("Enter your 2nd number: "))

if operators == "+":
    result = num1 + num2
    print(round(result, 3))
elif operators == "-":
    result = num1 - num2
    print(round(result, 3))
elif operators == "/":
    result = num1 / num2
    print(round(result, 3))
elif operators == "*":
    result = num1 * num2
    print(round(result, 3))
elif operators == "//":
    result = num1 // num2
    print(round(result, 3))
elif operators == "**":
    result = num1 ** num2
    print(round(result, 3))
else:
    print(f"{operators} is not valid operators")    
    