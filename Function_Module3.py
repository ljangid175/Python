from Marvellous import addition

def main():
    print("Enter First Number:")
    Value1 = int(input())
    print("Enter Second Number:")
    Value2 = int(input())
    ret = addition(Value1, Value2)
    print("Sum is:", ret)
    ret = substraction(Value1, Value2) # Error
    print("Diff is:", ret)


if __name__ == "__main__":
    main()
