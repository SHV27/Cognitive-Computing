import random

num = random.randint(1, 50)

def check_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

if check_prime(num):
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")
