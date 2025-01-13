try:
    num = int(input("Enter numerator: "))
    denom = int(input("Enter denominator: "))
    result = num / denom
    print("Result:", result)
except ZeroDivisionError:
    print("Cannot divide by zero.")
except ValueError:
    print("Please enter valid integers.")
