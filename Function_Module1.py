import Marvellous

def main():
    print("Enter First Number:")
    Value1 = int(input())
    print("Enter Second Number:")
    Value2 = int(input())
    ret = Marvellous.addition(Value1, Value2)
    print("Sum is:", ret)
    return

if __name__ == "__main__":
    main()
