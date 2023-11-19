# names = []


# for _ in range(3):
#     # name = input("What is your name? ")
#     # names.append(name)
#     names.append(input("What is your name? "))

# for name in names:
#     print(f"hello, {name}")


# name = input("What is your name? ")

# file = open("name.txt", "w") # lưu cái mơi nhất
# lưu tất cả các thông tin dc nhập sau mỗi lần gọi
# file = open("name.txt", "a")
# file.write(f"{name}\n")
# file.close()


# with open("name.txt", "a") as file:
#     file.write(f"{name}\n")


# Đọc file.txt
# with open("name.txt", "r") as file:
#     lines = file.readlines()


# for line in lines:
#     print("hello", line.rstrip())


#   Đọc file.txt cach 2
# with open("name.txt", "r") as file:
#     for line in file:
#         print("hello", line.rstrip())


names = []
with open("name.txt", "r") as file:
    for line in file:
        names.append(line.rstrip())

#  Sap xep theo thu tu bang chu cai
# for name in sorted(names):
#     print(f"Hello, {name}")


#  Sap xep theo thu tu bang chu cai nguoc lai
for name in sorted(names, reverse=True):
    print(f"Hello, {name}")