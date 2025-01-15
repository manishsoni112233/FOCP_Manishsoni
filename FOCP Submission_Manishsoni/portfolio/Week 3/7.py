def multiplication():
    num= int(input("Enter a number between 0 to 12 to find the multiplication table: "))
    if num>=-12 and num<=12:
        if num>=0:
            for i in range(13):
                result= i*num
                print(f"{i} x {num}= {result}")
        else:
            for i in range(12,-1, -1):
                result = i*num
                print(f"{i}x{num}={result}")
    else:
        print("Invalid number. Plaese enter a valur between -12 and 12")

multiplication()