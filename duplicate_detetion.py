print("enter number to make the list")
a = []
for i in range(5):
    num = int(input())
    a.append(num)
duplicate=0
for i in range(len(a)):
    if (duplicate<0):
        remove = a[i]
print("the list is", a)

