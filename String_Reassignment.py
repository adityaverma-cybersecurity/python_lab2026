def  change_string(s):
    if len(s) > 0: #CHECKING IF THE STRING IS NOT EMPTY
        new_string = s.replace(s[0], 'X',1)
        return new_string

    
string = input("Enter a string: ")
result = change_string(string)

print("The original string is:", string)
print("The modified string is:", result)