def main():
    Marks = [12, 44, 53, 5, 64]

    for no in Marks:
        print(no)
    
    Marks[2] = 34
    print("-"*15)
    for no in Marks:
        print(no)

if __name__ == "__main__":
    main()