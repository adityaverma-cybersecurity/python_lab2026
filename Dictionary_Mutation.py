def add_entry(d):
    name = input("Enter the name to add: ")
    age = int(input("Enter the age: "))
    d[name] = age


def reassign_dict(d):
    d = {"Alice": 20, "Bob": 25}
    print("Inside reassign_dict():", d)


# Create dictionary
age_dic = {}

num = int(input("Enter the number of people: "))

for i in range(num):
    name = input(f"Enter the name of person {i + 1}: ")
    age = int(input(f"Enter the age of {name}: "))
    age_dic[name] = age

print("\nOriginal dictionary:", age_dic)

# Test add_entry()
add_entry(age_dic)

print("After add_entry():", age_dic)

# Test reassign_dict()
reassign_dict(age_dic)

print("After reassign_dict():", age_dic)