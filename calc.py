import math
print("best calculator ever!")
x = int(input("x: "))
y = int(input("y: "))

print(f"Sum: {x + y}")
print(f"sub: {x - y}")
print(f"mult: {x * y}")
if y == 0:
    print("Cant do it")
else:
    print(f"div: {x / y}")

print(f"SQTR: {math.sqrt(x)}")

