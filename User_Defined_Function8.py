def BigBazar():
    print("Inside Big Bazaar")

    def Amul():
        print("Inside Amul Icecream Parlour")

def main():
    BigBazar()          # Allowed
    Amul()              # Error
    BigBazar.Amul()     # Error
    
if __name__ == "__main__":
    main()