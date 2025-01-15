import sys

sys.argv = ["count_args.py","arg1","arg2","arg3","arg4"] 

num_arguments = len(sys.argv) - 1

print(f"Number of arguments provided: {num_arguments}")
