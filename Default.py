def Area(Radius, PI=3.14):
    Ans = PI * Radius * Radius
    return Ans

def main():
    ret = Area(10.5)
    print("Area of circle is:", ret)
    ret = Area(10.5, 7.12)
    print("Area of circle is:", ret)


if __name__ == "__main__":
    main()