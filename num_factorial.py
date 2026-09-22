def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

n = int(input("Enter a non-negative integer: "))
if n < 0:
    print("Factorial is not defined for negative numbers.")
else:
    result = factorial(n)
    print(f"The factorial of {n} is: {result}")