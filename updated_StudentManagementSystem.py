class Student:
    def __init__(self, roll_no, name, course):
        self.roll_no = roll_no
        self.name = name
        self.course = course

    def display_info(self):
        print(f"Roll No: {self.roll_no}, Name: {self.name}, Course: {self.course}")

# Management system class
class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self, roll_no, name, course):
        student = Student(roll_no, name, course)
        self.students.append(student)
        print("Student added successfully.")

    def display_all(self):
        if not self.students:
            print("No student record found.")
        else:
            for student in self.students:
                student.display_info()

    def search_student(self, roll_no):
        for student in self.students:
            if student.roll_no == roll_no:
                student.display_info()
                return
        print("Student not found!")

    def delete_student(self, roll_no):
        for student in self.students:
            if student.roll_no == roll_no:
                self.students.remove(student)
                print("Student deleted.")
                return
        print("Student not found.")

    def update_student(self, roll_no, name, course):
        for student in self.students:
            if student.roll_no == roll_no:
                student.name = name
                student.course = course
                print("Student updated.")
                return
        print("Student not found.")

# Menu for user interaction
def menu():
    sms = StudentManagementSystem()

    while True:
        print("\n-------- Student Management System --------")
        print("1. Add student")
        print("2. Display all students")
        print("3. Search student")
        print("4. Delete student")
        print("5. Update student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            roll = input("Enter Roll No: ")
            name = input("Enter Name: ")
            course = input("Enter Course: ")
            sms.add_student(roll, name, course)

        elif choice == '2':
            sms.display_all()

        elif choice == '3':
            roll = input("Enter Roll No to search: ")
            sms.search_student(roll)

        elif choice == '4':
            roll = input("Enter Roll No to delete: ")
            sms.delete_student(roll)

        elif choice == '5':
            roll = input("Enter Roll No to update: ")
            name = input("Enter New Name: ")
            course = input("Enter New Course: ")
            sms.update_student(roll, name, course)

        elif choice == '6':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

# Start the program
menu()
