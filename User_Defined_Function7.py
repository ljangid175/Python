def calculation(No1, No2):
    multiplication = No1 * No2
    division = No1 / No2

    return multiplication, division

def main():
    Value1 = int(input("Enter First No:"))
    Value2 = int(input("Enter Second No:"))
    ret1, ret2 = calculation(Value1, Value2)
    print("Multiplication is: ", ret1, "Division is :", ret2)
    
if __name__ == "__main__":
    main()