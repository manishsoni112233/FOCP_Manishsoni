import sys

sys.argv = ["shortest_arg.py", "srijal", "manish", "batsal", "shivraj", "aryan"]

arguments = sys.argv[1:]

if arguments:
    arguments.sort(key=len)
    print(f"The shortest argument is: {arguments[0]}")
else:
    print("No arguments were provided.")
