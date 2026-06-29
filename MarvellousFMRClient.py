from MarvellousLib import filterX, mapX, reduceX

CheckEven = lambda No: (No % 2 == 0)

Increment = lambda No: No + 1

Addition = lambda No1, No2: No1+No2

def main():
    Data = [10,23,13, 28, 53, 22]

    print("Input Data is:", Data)

    FData = list(filterX(CheckEven, Data))

    print("Data after filter:", FData)

    MData = list(mapX(Increment, FData))

    print("Data after map:", MData)

    RData = reduceX(Addition,MData)

    print("Data after reduce:", RData)

if __name__ == "__main__":
    main()