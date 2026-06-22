# hetrogenius is everything except string
def main():
    Data1 = [10, 3.14, True, "Pune"]        # List (hetrogenius)
    Data2 = (10, 3.14, True, "Pune")        # Tuple (hetrogenius)
    print(Data1)
    print(Data2)

    print(Data1[0])
    print(Data2[0])

if __name__ == "__main__":
    main()