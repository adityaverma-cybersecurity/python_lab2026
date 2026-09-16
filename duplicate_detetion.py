
print("Enter 5 numbers to make the list")

a = []

for i in range(5):
    num = int(input())
    a.append(num)

i = 0

while i < len(a):
    j = i + 1

    while j < len(a):
        if a[i] == a[j]:
            a.remove(a[j])
        else:
            j += 1

    i += 1

print("The list is:", a)
