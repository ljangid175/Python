def Summation(Data):
    sum = 0
    
    for j in range(len(Data)):
        sum = sum + Data[j]
    
    return sum

def main():
    Size = 0
    Arr = list()

    print("Enter the Number of elements")
    Size = int(input())

    print("Enter the Elements")

    for i in range(Size):
        no = int(input())
        Arr.append(no)
    
    Ret = Summation(Arr)

    print("Sum is:", Ret)

if __name__ == "__main__":
    main()