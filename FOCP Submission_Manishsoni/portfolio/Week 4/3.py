name = input("Enter your name: ")
newname = ""
for x in range(len(name)):
    if x == 0:
        letter= name[x].upper()  # Capitalize the first letter
    else:
        letter  = name[x].lower()
    newname=newname+letter
      
print(newname)
