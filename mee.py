
# Student Record Management System (CRUD)

students = []

# ------------------ Add Student ------------------
def add_student(students):
    student_id = int(input("Enter Student ID: "))
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    marks = float(input("Enter Marks: "))

    if age > 0 and 0 <= marks <= 100:
        student = {
            "id": student_id,
            "name": name,
            "age": age,
            "marks": marks
        }
        students.append(student)
        print("Student added successfully!")
    else:
        print("Invalid Age or Marks!")

# ------------------ View Students ------------------
def view_students(students):
    if len(students) == 0:
        print("No student records found.")
    else:
        print("\nStudent Records")
        for student in students:
            print("----------------------------")
            print("ID:", student["id"])
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Marks:", student["marks"])

# ------------------ Update Student ------------------
def update_student(students):
    student_id = int(input("Enter Student ID to update: "))

    for student in students:
        if student["id"] == student_id:
            print("Student Found!")

            student["name"] = input("Enter New Name: ")
            student["age"] = int(input("Enter New Age: "))
            student["marks"] = float(input("Enter New Marks: "))

            if student["age"] > 0 and 0 <= student["marks"] <= 100:
                print("Student updated successfully!")
            else:
                print("Invalid Age or Marks!")
            return

    print("Student ID not found.")

# ------------------ Delete Student ------------------
def delete_student(students):
    student_id = int(input("Enter Student ID to delete: "))

    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            print("Student deleted successfully!")
            return

    print("Student ID not found.")

# ------------------ Search Student ------------------
def search_student(students):
    name = input("Enter Student Name: ")

    found = False

    for student in students:
        if student["name"].lower() == name.lower():
            print("----------------------------")
            print("ID:", student["id"])
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Marks:", student["marks"])
            found = True

    if not found:
        print("Student not found.")

# ------------------ Average Marks ------------------
def average_marks(students):
    if len(students) == 0:
        print("No records available.")
        return

    total = 0

    for student in students:
        total += student["marks"]

    avg = total / len(students)

    print("Average Marks =", avg)

# ------------------ Show Topper ------------------
def show_topper(students):
    if len(students) == 0:
        print("No records available.")
        return

    topper = students[0]

    for student in students:
        if student["marks"] > topper["marks"]:
            topper = student

    print("\nTopper Details")
    print("----------------------------")
    print("ID:", topper["id"])
    print("Name:", topper["name"])
    print("Age:", topper["age"])
    print("Marks:", topper["marks"])

# ------------------ Main Menu ------------------
while True:

    print("\n===== Student Record Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Search Student")
    print("6. Calculate Average Marks")
    print("7. Show Topper")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student(students)

    elif choice == "2":
        view_students(students)

    elif choice == "3":
        update_student(students)

    elif choice == "4":
        delete_student(students)

    elif choice == "5":
        search_student(students)

    elif choice == "6":
        average_marks(students)

    elif choice == "7":
        show_topper(students)

    elif choice == "8":
        print("Thank you!")
        break

    else:
        print("Invalid Choice!")