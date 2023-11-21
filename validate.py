import re

# .strip()  bỏ khoảng trắng đầu cuối
email = input("What is your email? ").strip()


username, domain = email.split("@")


# if username and "." in domain:
#     print("Valid")
# else:
#     print("Invalid")


# if username and domain.endswith(".edu"):
#     print("Valid")
# else:
#     print("Invalid")


if re.search(".+@.+.edu", email): # Chỉ cần chứa @ trong chuỗi là trả về True
    print("Valid")
else:
    print("Invalid")
