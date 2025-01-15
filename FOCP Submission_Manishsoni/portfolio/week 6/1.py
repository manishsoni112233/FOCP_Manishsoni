def int_to_binary(n):
    if n <= 0:
        raise ValueError("Input must be a positive integer.")
    return bin(n)[2:]

number = 10
binary_representation = int_to_binary(number)
print(f"The binary representation of {number} is {binary_representation}.")
