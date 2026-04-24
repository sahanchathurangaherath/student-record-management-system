# Project Planner

Project Name:
Student Record Management System

Problem Statement:
Many schools, tutors, and small training centers need a simple way to store and manage student information. Manual record keeping is slow and confusing, especially when searching, updating, or deleting student details. This project solves the problem by creating a basic Python command-line application to manage student records in an organized way.

Objective:
To build a simple Python CLI application that allows users to add, view, search, update, delete, and save student records using file handling.

## Features:

- Add a new student
- View all students
- Search student by ID or name
- Update student details
- Delete student record
- Save records to a file
- Load existing records from file

## Functions:

- add_student()
- view_students()
- search_student()
- update_student()
- delete_student()
- save_students()
- load_students()
- main_menu()

To-Do:

- [x] Plan project
- [x] Create menu
- [x] Build features
- [x] Test program
- [x] Fix bugs
- [x] Final review

Progress Notes:
The project was developed as a simple Python command-line application. First, the menu system was created. Then student record functions were added one by one. File handling was added to save and load records.

Problems and Fixes:
- Problem: Data was lost after closing the program.
  Fix: Added file handling to save records.
- Problem: Searching students manually was difficult.
  Fix: Added search function using student ID or name.
- Problem: Invalid menu inputs caused issues.
  Fix: Added input validation.

Future Improvements:
- Add database support
- Add login system
- Add GUI interface
- Export records as CSV or PDF
- Add student marks and grade management