def countdown(n):
    while n > 1:
        
        n -= 1
        yield n

num = int(input("Enter a number to countdown from: "))
for i in countdown(num):
    print(i)
