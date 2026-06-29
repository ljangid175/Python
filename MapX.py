def CheckEven(No): 
    return (No % 2 == 0)

def Increment(No):
    return No + 1

def main():
    Data = [10,23,13, 28, 53, 22]

    print("Input Data is:", Data)

    FData = list(filter(CheckEven, Data))

    print("Data after filter:", FData)

    MData = list(map(Increment, FData))

    print("Data after amp:", MData)

if __name__ == "__main__":
    main()