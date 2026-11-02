# Add new employee
def add_employee():
    employee_id = input("Employee ID: ")
    name = input("Name: ")
    position = input("Position: ")
    salary = input("Salary: ")

    record = employee_id + ", " + name + ", " + position + ", " + salary + "\n"

    with open("employees.txt", "a") as f:
        f.write(record)
    print("Employee record added successfully!")


# View all employees
def view_employees():
    with open("employees.txt", "r") as f:
        print(f.read())

# Search one employee by id
def search_by_id():
    search_id = input("Enter Employee ID to search: ")
    found = False

    with open("employees.txt", "r") as f:
        for line in f:
            parts = line.split(',')
            if parts[0].strip() == search_id:
                print(line)
                found = True
                break 

    if not found:
        print("Employee not found.")


# Update information
def update_employee():
    update_id = input("Enter Employee ID to update: ")
    found = False

    with open("employees.txt", "r") as f:
        lines = f.readlines()

    with open("employees.txt", "w") as f:
        for line in lines:
            parts = line.split(",")
            if parts[0].strip() == update_id:
                found = True
                print("Current record:", line)
                name = input("New Name (leave blank to keep current): ") or parts[1].strip()
                position = input("New Position (leave blank to keep current): ") or parts[2].strip()
                salary = input("New Salary (leave blank to keep current): ") or parts[3].strip()

                new_line = update_id + ", " + name + ", " + position + ", " + salary + "\n"
                f.write(new_line)
            else:
                f.write(line)

    if not found:
        print("Employee not found.")
    else:
        print("Employee record updated successfully!")

# Update information
def delete_employee():
    delete_id = input("Enter Employee ID to delete: ")
    found = False

    with open("employees.txt", "r") as f:
        lines = f.readlines()

    with open("employees.txt", "w") as f:
        for line in lines:
            parts = line.split(",")
            if parts[0].strip() == delete_id:
                found = True
                continue
            else:
                f.write(line)

    if not found:
        print("Employee not found.")
    else:
        print("Employee record deleted successfully!")



while True:
    print("1. Add new employee record")
    print("2. View all employee records")
    print("3. Search for an employee by Employee ID")
    print("4. Update an employee's information")
    print("5. Delete an employee record")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_employee()
    elif choice == "2":
        view_employees()
    elif choice == "3":
        search_by_id()
    elif choice == "4":
        update_employee()
    elif choice == "5":
        delete_employee()
    elif choice == "6":
        print("Exiting program...")
        break
    else:
        print("Invalid choice, try again.")