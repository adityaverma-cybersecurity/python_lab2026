def double_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * 2
    return wrapper

@double_result
def add(a, b):
    return a + b
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(f"The double of the sum of {a} and {b} is: {add(a, b)}")
