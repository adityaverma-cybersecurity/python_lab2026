
def add_entry(name, age):
    age_dic[name] = age



age_dic={}
num=int(input("Enter the number of people: "))
for i in range(num):
    name = input("Enter the name of person {}: ")
    age = int(input("Enter the age of {}:  "))
    age_dic[name] = age

print("The dictionary of names and ages is:", age_dic)
add_entry("John", 30)
print("The updated dictionary after adding John is:", age_dic)