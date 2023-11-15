

# hello()
# name = input("What is your name? ")
# hello(name)   



# def main():
#     name = input("What is your name? ")
#     hello(name)


def hello(name= "world"):
    print("Hello, ", name)




def main():
    x = int(input("What is x? "))
    print("x squared is", square(x))



def square(n):
    # return n * n
    return pow(n, 2) # n^2

main()    