def CheckEven(No):
    if (No % 2 == 0):
        print("It's Even Number")
    else:
        print("It's Odd number")

def main():
    Value = int(input("Enter number:"))
    
    CheckEven(Value)

if __name__ == "__main__":
    main()