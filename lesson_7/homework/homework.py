import math

class Vector():
    def __init__(self, *components):
        if not components:
            raise ValueError("Vektor kamida bitta o'lchamga ega bo'lishi kerak. ")

        self.components = tuple(x for x in components)

    def __len__(self):
        return len(self.components)
    

    def __add__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vektorlar bir xil o'lchamda bo'lishi kerak.")
        new_components = tuple(a + b for a, b in zip(self.components, other.components))
        return Vector(*new_components)

    def __sub__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vektorlar bir xil o'lchamda bo'lishi kerak.")
        new_components = tuple(a - b for a, b in zip(self.components, other.components))
        return Vector(*new_components)
        
    def __mul__(self, other):
        if(len(self.components) != len(other.components)):
            raise ValueError("Vektorlar bir xil o'lchamda bo'lishi kerak.")
        new_components = tuple(a * b for a, b in zip(self.components, other.components))
        return sum(new_components)

    def __str__(self):
        return f"Vector({", ".join(str(c) for c in self.components)})"
    
    def scl_mul(self, other):
        new_components = tuple(a*other for a in self.components)
        return Vector(*new_components)
        
    def magnitude(self):
        # return math.sqrt(self.x**2 + self.y**2)
        quadrat_components = tuple(a**2 for a in self.components)
        new_components = math.sqrt(sum(quadrat_components))
        return new_components

    def normalize(self):
        deviation = self.magnitude()
        if deviation == 0:
            raise ValueError("Nol vektorni normalize qilib bo'lmaydi.")
        new_components = tuple(f'{a/deviation:.3f}' for a in self.components)
        return Vector(*new_components)

# Create vectors
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

# Print the vector
print(v1)

# Addition
v3 = v1 + v2
print(v3)

# Subtraction
v4 = v2 - v1
print(v4)

# Dot product
dot_product = v1 * v2
print(dot_product)

# Magnitude
print(v1.magnitude())

# Normalization
print(v1.normalize())



# Employee Manager Application (OOP version)
class Employee():
    def __init__(self, id, name, position, salary):
        self.id = id
        self.name = name
        self.position = position
        self.salary = salary

    def append(self):
        with open("employees.txt", "a") as f:
                user = f"{self.id}, {self.name}, {self.position}, {self.salary}\n"
                f.write(user)
                print(f"Successfully added: {user}")

class EmployeeManager():
    def __init__(self, id=None, name=None, position=None, salary=None):
        self.id = id
        self.name = name
        self.position = position
        self.salary = salary
        
    def read(self):
        with open("employees.txt", "rt") as f:
            content = f.read()
        return content if content else "No records found\n"

    def search_by_id(self):
        with open("employees.txt") as f:
            for x in f.readlines():
                if x.split(",")[0].strip() == str(self.id):
                    return x
        return "User not found\n"

    def delete_by_id(self):
        with open("employees.txt") as f:
            lines = f.readlines()
        found = False
        with open("employees.txt", "w") as f:
            for line in lines:
                if line.split(",")[0].strip() != str(self.id):
                    f.write(line)
                else:
                    found = True
        print("Successfully Deleted\n" if found else "User not found\n")

    def update_by_id(self):
        with open("employees.txt") as f:
            lines = f.readlines()
        updated = False
        with open("employees.txt", "w") as f:
            for line in lines:
                parts = line.strip().split(",")
                emp_id = parts[0].strip()

                if emp_id == str(self.id):
                    name = self.name if self.name else parts[1].strip()
                    position = self.position if self.position else parts[2].strip()
                    salary = self.salary if self.salary else parts[3].strip()

                    new_line = f"{emp_id}, {name}, {position}, {salary}\n"
                    f.write(new_line)
                    updated = True
                else:
                    f.write(line)
        print("Successfully updated\n" if updated else "User not found\n")

    def run(self):
        while True:
            print("1. Add\n2. View\n3. Search\n4. Update\n5. Delete\n6. Exit")
            choice = input("Select: ")
            print("\n")
            if choice == "6":
                break
            elif choice == "1":
                self.id = str(input("ID: "))
                self.name = str(input("Name: "))
                self.position = str(input("Position: "))
                self.salary = input("Salary: ")
                user = Employee(self.id, self.name, self.position, self.salary)
                user.append()
            elif choice == "2":
                print(self.read())
            elif choice == "3":
                self.id = input("Searching ID: ")
                print(self.search_by_id())
            elif choice == "4":
                self.id = str(input("ID: "))
                self.name = str(input("Name (bo'sh qoldiring, o'zgartirmasangiz): "))
                self.position = str(input("Position: "))
                self.salary = input("Salary: ")
                self.update_by_id()
            elif choice == "5":
                self.id = input("Deleting ID: ")
                self.delete_by_id()

manager = EmployeeManager()
manager.run()

class Task():
    def __init__(self, id, title, description, status, date=None,):
        self.id = id
        self.title = title
        self.description = description
        self.status = status 
        self.date = date

class TaskManager():
    def __init__(self):
        self.tasks = []

    def add_task(self, id, title, description, status, date=None):
        new_task = Task(id, title, description, status, date)
        self.tasks.append(new_task)
        print("Task added successfully\n")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found\n")
            return
        for task in self.tasks:
            print(f"{task.id}, {task.title}, {task.description}, {task.status}, {task.date}\n")

    def delete_by_id(self, id):
        found = any(task.id == str(id) for task in self.tasks)
        self.tasks = [task for task in self.tasks if task.id != str(id)]
        print("Successfully Deleted\n" if found else "Task not found\n")

    def update_by_id(self, id, title=None, description=None, status=None, date=None):
        updated = False
        for task in self.tasks:
            if task.id == str(id):
                task.title = title if title else task.title
                task.description = description if description else task.description
                task.status = status if status else task.status
                task.date = date if date else task.date
                updated = True
        print("Successfully updated\n" if updated else "Task not found\n")

    def filter_by_status(self, status):
        found = False
        for task in self.tasks:
            if task.status == status:
                print(f"{task.id}, {task.title}, {task.description}, {task.date}, {task.status}")
                found = True
        if not found:
            print("No tasks found with this status\n")

    def save(self):
        with open("tasks.txt", "w") as f:
            for task in self.tasks:
                f.write(f"{task.id}, {task.title}, {task.description}, {task.status}, {task.date}\n")
            print("Tasks saved successfully\n")

    def load(self):
        self.tasks = []
        try:
            with open("tasks.txt") as f:
                for line in f.readlines():
                    parts = line.strip().split(",")
                    task = Task(parts[0].strip(), parts[1].strip(),parts[2].strip(), parts[3].strip(), parts[4].strip())
                    self.tasks.append(task)
            print("Tasks loaded successfully\n")
        except FileNotFoundError:
            print("No saved file found, starting fresh.\n")

    def run(self):
        while True:
            print("1. Add a new task\n2. View all tasks\n3. Update a task\n4. Delete a task\n5. Filter by status\n6. Save tasks\n7. Load tasks\n8. Exit")
            choice = input("Select: ")
            print("\n")
            if choice == "8":
                break
            elif choice == "1":
                id = str(input("Enter Task ID: "))
                title = str(input("Enter Title: "))
                description = str(input("Enter Description: "))
                status = input("Enter status (Pending/In Progress/Completed): ")
                date = input("Enter Due Date(YYYY-MM-DD): ")
                self.add_task(id, title, description, status, date)
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                id = str(input("Which Task ID do you want to update?: "))
                title = str(input("New Title (leave blank to keep current): "))
                description = str(input("New Description (leave blank to keep current): "))
                status = input("New Status (leave blank to keep current): ")
                date = input("New Due Date(YYYY-MM-DD) (leave blank to keep current): ")
                self.update_by_id(id, title, description, status, date)
            elif choice == "4":
                id = input("Deleting ID:")
                self.delete_by_id(id)
            elif choice == "5":
                status = input("Enter status (Pending/In Progress/Completed): ")
                self.filter_by_status(status)
            elif choice == "6":
                self.save()
            elif choice == "7":
                self.load()
    
task_manager = TaskManager()
task_manager.run()
