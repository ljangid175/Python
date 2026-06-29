CheckEven = lambda No: (No % 2 == 0)

def main():
    Value = int(input("Enter number:"))
    
    Ret = CheckEven(Value)

    if (Ret==True):
        print("It's Even Number")
    else:
        print("It's Odd Number")

if __name__ == "__main__":
    main()