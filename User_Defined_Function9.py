def BigBazar():
    print("Inside Big Bazaar")

    def Amul():
        print("Inside Amul Icecream Parlour")
    
    Amul()
    Amul()

def main():
    BigBazar()          # Allowed
    
if __name__ == "__main__":
    main()