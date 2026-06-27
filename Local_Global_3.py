no = 11     # Global Variable

def Display():
    no = 21
    print("From Display: ", no) # will chase the nearest variable


print("Before: ", no) # 11
Display()             # 21
print("After: ", no)  # 11