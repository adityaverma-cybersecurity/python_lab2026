def show_info(func):
    def wrapper():
        print("Calling function...")
        func()
        print("Function executed.")
    
    return wrapper


@show_info
def hello():
    print("Hello, Python!")


hello()