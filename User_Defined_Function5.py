# Accept : Multiple Parameter
# Returns : Multiple values

def marvellous(no1,no2):
    print("Inside Marvellous:", no1, no2)
    return 21, 51

def main():
    ret1,ret2 = marvellous(11, 10)
    print("Returned values are:", ret1,ret2)

if __name__ == "__main__":
    main()