def Summation(Data):
    sum = 0
    for i in range(len(Data)):
        sum = sum + Data[i]
    return sum

def main():
    Marks = [12, 44, 53, 5, 64]

    ret = Summation(Marks)
    
    print("Sum is:", ret)

if __name__ == "__main__":
    main()