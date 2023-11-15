# i = 0


# while i < 3:
#     print("meow")
#     i += 1


# # for i in [1,2,3]:
# for i in range(3):
#     print("meow")


# print("meow \n" * 3, end="")


# while True:
#     n = int(input("What is n? "))
#     if n > 0:
#         break


# for _ in range(n):
#     print("meow-----")


def main():
    number = get_numbers()
    meow(number)


def get_numbers():
    while True:
        n = int(input("What is n? "))
        if n > 0:
            break
    return n    


def meow(n):
    for i in range(n):
        print('meow')


main()
