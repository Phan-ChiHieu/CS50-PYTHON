# x = int(input("What is x? "))


# if x % 2 == 0:
#     print("Even")
# else:
#     print("Odd")




def main(): 
    x = int(input("What is x? ")) 
    if is_even(x):
        print("Even")
    else:
        print("Odd")


def is_even(n):
    #  Cach 1:
    # if n % 2 == 0:
    #     return True
    # else:
    #     return False

    #  Cach 2:
    # return True if n % 2 == 0 else False

    #  Cach 3:
    return n % 2 == 0


main()


# 2:39