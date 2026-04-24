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