def main():
    name = input("What is your name? ")
    output = hello(name)
    print(output)


def hello(to="world"):
    return f"Hello, {to}"


if __name__ == "__main__":
    main()
