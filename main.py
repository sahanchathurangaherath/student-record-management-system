
import os

FILE_NAME = "students.txt"



def load_students():
    students = []

    if not os.path.exists(FILE_NAME):
        return students

    with open(FILE_NAME, "r") as file:
        for line in file:
            data = line.strip().split(",")
            if len(data) == 4:
                student = {
                    "id": data[0],
                    "name": data[1],
                    "age": data[2],
                    "course": data[3]
                }
                students.append(student)

    return students


def save_students(students):
    with open(FILE_NAME, "w") as file:
        for student in students:
            file.write(
                f"{student['id']},{student['name']},{student['age']},{student['course']}\n"
            )


def add_student(students):
    print("\n--- Add Student ---")

    student_id = input("Enter Student ID: ")

    for student in students:
        if student["id"] == student_id:
            print("Student ID already exists!")
            return

    name = input("Enter Student Name: ")
    age = input("Enter Student Age: ")
    course = input("Enter Course: ")

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "course": course
    }

    students.append(student)
    save_students(students)

    print("Student added successfully!")

def add_student(students):
    print("\n--- Add Student ---")

    student_id = input("Enter Student ID: ")

    for student in students:
        if student["id"] == student_id:
            print("Student ID already exists!")
            return

    name = input("Enter Student Name: ")
    age = input("Enter Student Age: ")
    course = input("Enter Course: ")

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "course": course
    }

    students.append(student)
    save_students(students)

    print("Student added successfully!")


def view_students(students):
    print("\n--- All Students ---")

    if not students:
        print("No student records found.")
        return

    for student in students:
        print("----------------------")
        print("ID     :", student["id"])
        print("Name   :", student["name"])
        print("Age    :", student["age"])
        print("Course :", student["course"])


def search_student(students):
    print("\n--- Search Student ---")

    search_value = input("Enter Student ID or Name: ").lower()

    found = False

    for student in students:
        if student["id"].lower() == search_value or student["name"].lower() == search_value:
            print("----------------------")
            print("ID     :", student["id"])
            print("Name   :", student["name"])
            print("Age    :", student["age"])
            print("Course :", student["course"])
            found = True

    if not found:
        print("Student not found.")


def update_student(students):
    print("\n--- Update Student ---")

    student_id = input("Enter Student ID to update: ")

    for student in students:
        if student["id"] == student_id:
            print("Student found. Enter new details.")

            student["name"] = input("Enter New Name: ")
            student["age"] = input("Enter New Age: ")
            student["course"] = input("Enter New Course: ")

            save_students(students)
            print("Student updated successfully!")
            return

    print("Student not found.")



def delete_student(students):
    print("\n--- Delete Student ---")

    student_id = input("Enter Student ID to delete: ")

    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            save_students(students)
            print("Student deleted successfully!")
            return

    print("Student not found.")




def main_menu():
    students = load_students()

    while True:
        print("\n==============================")
        print(" Student Record Management")
        print("==============================")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            update_student(students)
        elif choice == "5":
            delete_student(students)
        elif choice == "6":
            save_students(students)
            print("Thank you! Program closed.")
            break
        else:
            print("Invalid choice. Please try again.")

main_menu()