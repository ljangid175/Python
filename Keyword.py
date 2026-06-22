def Area(Radius, PI):
    Ans = PI * Radius * Radius
    return Ans

def main():
    ret = Area(PI=3.14, Radius=10.5)
    ret = Area(10.5,PI=3.14)            # Allowed
    ret = Area(PI=3.14, 10.5)            # Error
    print("Area of circle is:", ret)


if __name__ == "__main__":
    main()