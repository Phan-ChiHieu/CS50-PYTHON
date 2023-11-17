def main():
    x = get_int("What is x? ")
    print(f"x is {x}")


def get_int(promt):
    while True:
        try:
            return int(input(promt))
        except ValueError:
            # print("x is not an integer")
            pass


main()
