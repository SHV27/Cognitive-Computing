numbers = []
print("Enter five numbers:")
for i in range(5):
    num = int(input("Number: "))
    numbers.append(num)
print("Numbers:", numbers)
print("Largest number:", max(numbers))
print("Smallest number:", min(numbers))
