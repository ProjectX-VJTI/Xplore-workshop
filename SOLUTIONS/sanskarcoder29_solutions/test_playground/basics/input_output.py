integer = int(input("Enter an integer: "))
print(type(integer))

number = float(input("Enter a number (floating point allowed): "))
print(type(number))

array = list(map(int, input("Enter an array of numbers: ").split()))
print(type(array))

nums = [1,2,3,4]
print(",".join(map(str, nums)))

name = input("Enter your name: ")
print(f"Hello, {name}")

x, y, z = 67, 420, 9000
print(x, y, z, sep="\n\n")