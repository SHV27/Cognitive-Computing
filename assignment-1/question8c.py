try:
    num = int(input("Enter the numerator: "))
    denom = int(input("Enter the denominator: "))
    res = num / denom
    print("Result:", res)
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Please enter valid integers.")
finally:
    print("This block always runs.")
