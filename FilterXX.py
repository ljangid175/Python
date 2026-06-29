CheckEven = lambda No : (No % 2 == 0)

def main():
    Data = [10,23,13, 28, 53, 22]

    print("Input Data is:", Data)

    FData = list(filter(CheckEven, Data))

    print("Input Data is:", FData)

if __name__ == "__main__":
    main()