import csv

# name = input("what is your name? ")
# home = input("what is your home? ")


# with open("student2.csv", "a") as file:
#     writer = csv.writer(file)
#     writer.writerow([name, home])

# csv
# Edric,USA

# Minh,SaiGon


# with open("student2.csv", "a") as file:
#     writer = csv.DictWriter(file, fieldnames=["name", "home"])
#     writer.writerow({"name": name, "home": home})

# csv
# Tuan,Xin Chao Moi Nguoi


#  Read

students = []

with open("student2.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})


for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")


# Edric is from USA
# Minh is from SaiGon
# Tuan is from Xin Chao Moi Nguoi




# 8:26