def even_numbers(limit):
    for num in range(2, limit + 1, 2):
        yield num

limit = int(input("Enter a limit to generate even numbers: "))
for even in even_numbers(limit):
    print(even)