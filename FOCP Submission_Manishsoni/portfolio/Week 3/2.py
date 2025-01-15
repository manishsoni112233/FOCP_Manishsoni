def password():
    pw1=input("Enter a new password: ")
    pw2=input("Please, confirm your password: ")
    if pw1==pw2:
        print("Password set")
    else:
        print("Error: Password doesn't match")

password()