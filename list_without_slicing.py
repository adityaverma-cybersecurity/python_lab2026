print("enter number to make the list")
a = []
for i in range(7):
    num = int(input())
    a.append(num)
for i in range(len(a)):
    print(a[len(a)-1-i])
