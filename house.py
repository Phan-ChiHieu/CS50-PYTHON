name = input("What is your name? ")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Hermione":
        print("Gryffindor")
    case "Draco":
        print("Slythrin")
    case _:
        print('Who?')
