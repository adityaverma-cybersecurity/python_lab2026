#creating a list of numbers by taking input form user 

print("enter number to make the list")
a = []
for i in range(10):
    num = int(input())
    a.append(num)
#finding the sum of the numbers in the list without using the sum() function
sum = 0
for i in range(len(a)):
    sum = sum + a[i]
print("The sum of the numbers in the list is:", sum)
#finding the average of the numbers in the list
print("The average of the numbers in the list is:", sum/len(a))