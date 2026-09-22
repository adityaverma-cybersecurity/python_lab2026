print("enter number to make the list")
a = []
for i in range(7):
    num = int(input())
    a.append(num)
#to short the list in ascending order using bubble sort algorithm
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]

print("The largest number in the list is:", a[-1])
print("The smallest number in the list is:", a[0])
