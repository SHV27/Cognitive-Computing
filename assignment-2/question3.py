import random

numbers = []
for i in range(100):
    numbers.append(random.randint(100, 900))

odds = []
evens = []
for num in numbers:
    if num % 2 == 0:
        evens.append(num)
    else:
        odds.append(num)

primes = []
for num in numbers:
    if num > 1:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)

print("Odd Numbers Count:", len(odds))
print("Even Numbers Count:", len(evens))
print("Prime Numbers Count:", len(primes))
