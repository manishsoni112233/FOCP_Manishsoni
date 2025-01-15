def user_name():
    name = input("Enter your name: ")
    if name.strip():
        print(f"Hello, {name}!")
    else:
        print(f"Hello, stranger!")

user_name()