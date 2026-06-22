def Area(Radius, PI):
    Ans = PI * Radius * Radius
    return Ans

def main():
    ret = Area(10.5, 3.14)
    print("Area of circle is:", ret)

    ret = Area(13.6, 7.12)
    print("Area of circle is:", ret)

if __name__ == "__main__":
    main()