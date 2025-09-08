import pyodbc

# Connection to SQL Server
con = pyodbc.connect(
    "Driver={SQL Server};"
    "Server=YOUR LOCAL SQL SERVER NAME;"   # Example: DESKTOP-123\\SQLEXPRESS
    "Database=StudentDB;"
    "Trusted_Connection=yes;"
)

cur = con.cursor()

def add_student():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    course = input("Enter course: ")
    marks = int(input("Enter marks: "))
    cur.execute("INSERT INTO Students (name, age, course, marks) VALUES (?, ?, ?, ?)", 
                (name, age, course, marks))
    con.commit()
    print("✅ Student added successfully!\n")

def view_students():
    cur.execute("SELECT * FROM Students")
    rows = cur.fetchall()
    if rows:
        print("ID | Name | Age | Course | Marks")
        for row in rows:
            print(row)
    else:
        print("No students found!\n")

def search_student():
    keyword = input("Enter ID or Name to search: ")
    if keyword.isdigit():
        cur.execute("SELECT * FROM Students WHERE student_id=?", (int(keyword),))
    else:
        cur.execute("SELECT * FROM Students WHERE name LIKE ?", ('%'+keyword+'%',))
    rows = cur.fetchall()
    if rows:
        for row in rows:
            print(row)
    else:
        print("No matching student found!\n")

def update_student():
    sid = int(input("Enter student ID to update: "))
    name = input("Enter new name: ")
    age = int(input("Enter new age: "))
    course = input("Enter new course: ")
    marks = int(input("Enter new marks: "))
    cur.execute("UPDATE Students SET name=?, age=?, course=?, marks=? WHERE student_id=?", 
                (name, age, course, marks, sid))
    con.commit()
    print("✅ Student updated successfully!\n")

def delete_student():
    sid = int(input("Enter student ID to delete: "))
    cur.execute("DELETE FROM Students WHERE student_id=?", (sid,))
    con.commit()
    print("🗑️ Student deleted successfully!\n")

def menu():
    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        
        choice = input("Enter choice: ")
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("👋 Exiting...")
            break
        else:
            print("Invalid choice! Try again.")

menu()
con.close()
