def remove_last(lst) :
    """
    Removes the last element from the list.

    """
    if lst:  # Check if the list is not empty
        lst.pop()  # Remove the last element

print("enter number to make the list")
lst= []
for i in range(5):
    num = int(input())
    lst.append(num)
print("The list before removing the last element:", lst)
remove_last(lst)
print("The list after removing the last element:", lst)