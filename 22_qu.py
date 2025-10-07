# Python program to display powers of 2 using anonymous function.

n = int(input("How many terms? "))
results = list(map(lambda x: 2 ** x, range(n)))
for i in range(n):
    print(f"2 raised to the power {i} is {results[i]}")
