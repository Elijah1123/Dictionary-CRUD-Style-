# dictionary_crud.py

def create_student():
    return {"id": 1, "name": "Elijah", "age": 22}


def read_student(student):
    return student


def update_student(student, key, value):
    student[key] = value
    return student


def delete_student(student, key):
    if key in student:
        del student[key]
    return student


student = create_student()
print(read_student(student))
print(update_student(student, "age", 25))
print(delete_student(student, "age"))