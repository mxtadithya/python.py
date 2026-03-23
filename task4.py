
try:
    file = open("students.txt", "x")
    file.close()
except:
    pass
while True:
    print("\n--- Student Menu ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")
    choice = input("Enter choice: ")
    # Step 2 & 3: Add student (append mode)
    if choice == "1":
        name = input("Enter student name: ")
        file = open("students.txt", "a")
        file.write(name + "\n")
        file.close()
        print("Student added!")
    # Step 4: View students
    elif choice == "2":
        try:
            file = open("students.txt", "r")
            content = file.read()
            file.close()
            if content == "":
                print("No students found.")
            else:
                print("\nStudent List:")
                print(content)
        except:
            print("File not found!")
    # Exit
    elif choice == "3":
        print("Exiting program...")
        break
    else:
        print("Invalid choice!")