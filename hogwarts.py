students = ["Hermione", "Harry", "Ron"]


# print(students[0])
# print(students[1])
# print(students[2])


# for student in students:
#     print(student)


for i in range(len(students)):
    print(1 + i, students[i])


students_obj = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}


# print(students_obj["Hermione"])
# print(students_obj["Harry"])
# print(students_obj["Ron"])
# print(students_obj["Draco"])


for student in students_obj:
    print(student, students_obj[student], sep=", ")
    
    


students_v3 = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]

for student in students_v3:
    print(student["name"], student["house"], student["patronus"], sep=", ")
    
