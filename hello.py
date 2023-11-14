# Khỏi tạo một biên name với input đầu vào do user nhập
name = input("What is your name? ")
print("hello," + name , end="\n")
print("Xin Chào,", name)

#  them f trong print(f"Text {parameters}")
print(f"Hi, {name}")

# Remove whitespace from str
#  Bỏ đi khoảng trắng đầu và cuối  string
# name = name.strip();


#  Capitalize user's name
#  Viết hoa chữ cái dầu tiên trong chuỗi
# name = name.capitalize()

#  Viết hoa toàn bộ chữ cái dầu trong chuỗi
# name = name.title()


#  Viết gọn lại
name = name.strip().title() # Edric Phan


first, last = name.split( " " )

print(f"First, {first}")

