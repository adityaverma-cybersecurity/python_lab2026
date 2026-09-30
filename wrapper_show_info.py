def show_info(func):
    def wrapper():
        print("Calling function...")
        func()
        print("Function executed.")
    
    return wrapper

num = int(input("Enter a number to square: "))


@show_info
def  square(num):
   return num * num


square(num)

