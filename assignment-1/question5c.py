numbers = []
print("Input 5 numbers:")
for i in range(5):
    num = int(input("Enter number: "))
    numbers.append(num)
print("Original list:", numbers)
print("Sorted in ascending order:", sorted(numbers))
print("Sorted in descending order:", sorted(numbers, reverse=True))
