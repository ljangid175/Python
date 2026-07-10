import os

a = 10
b = 10

print("CPU cores are", os.cpu_count())
print(id(a) == id(b)) # True, as same memory address is used