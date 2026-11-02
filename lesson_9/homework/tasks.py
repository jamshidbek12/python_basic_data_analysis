import json
import csv

class Task:
    def __init__(self, id, task, completed, priority):
        self.id = id
        self.task = task
        self.completed = completed
        self.priority = priority

class Manager:
    def __init__(self):
        self.tasks = []
        self.next_task_id = 1

    def create(self, task, completed_input, priority):
        try:
            task_id = self.next_task_id

            if not task:
                print("Error: Task name cannot be empty.")
                return

            if completed_input not in ["True", "False"]:
                print("You should enter 'True' or 'False' for 'completed' section")
                return

            if not isinstance(priority, int):
                print("Error: Priority must be a number.")
                return

            completed = True if completed_input == "True" else False
            task = Task(task_id, task, completed, priority)

            self.tasks.append({
                'id': task.id,
                'task': task.task,
                'completed': task.completed,
                'priority': task.priority
            })

            self.next_task_id += 1
            print(f"Task successfully created: id: {task.id}, task: {task.task}, completed: {task.completed}, priority: {task.priority}\n")

        except (TypeError, ValueError) as e:
            print(f"Error while creating task: {e}")

    def read(self):
        try:
            if not self.tasks:
                print("Tasks not found")
                return

            for task in self.tasks:
                print(f"{task['id']}, {task['task']}, {task['completed']}, {task['priority']}")

        except KeyError as e:
            print(f"Error: Missing field {e} in task data.")
        except TypeError as e:
            print(f"Error while reading tasks: {e}")

    def update(self, id, task, completed_input, priority):
        try:
            if completed_input not in ["True", "False", ""]:
                print("You should enter 'True' or 'False' for 'completed' section")
                return

            found = False

            if completed_input == "True":
                completed = True
            elif completed_input == "False":
                completed = False
            else:
                completed = None

            for row in self.tasks:
                if str(id) == str(row['id']):
                    row["task"] = task if task else row["task"]
                    row["completed"] = completed if completed is not None else row["completed"]
                    row["priority"] = priority if priority is not None else row["priority"]
                    found = True

            if not found:
                print(f"Task with {id} id not found")
            else:
                print(f"Task with {id} id successfully updated")

        except KeyError as e:
            print(f"Error: Missing field {e} in task data.")
        except (TypeError, ValueError) as e:
            print(f"Error while updating task: {e}")

    def delete(self, id):
        try:
            found = False

            for row in self.tasks:
                if str(row['id']) == str(id):
                    self.tasks.remove(row)
                    found = True
                    break

            if not found:
                print(f"Task with {id} id not found")
            else:
                print(f"Task with {id} id successfully deleted")

        except KeyError as e:
            print(f"Error: Missing field {e} in task data.")
        except (TypeError, ValueError) as e:
            print(f"Error while deleting task: {e}")

    def total_tasks(self):
        try:
            print(f"The total number of tasks: {len(self.tasks)}")
        except TypeError as e:
            print(f"Error while counting tasks: {e}")

    def completed_tasks(self):
        try:
            num = 0
            for row in self.tasks:
                if row['completed'] is True:
                    num += 1
            print(f"The number of completed tasks: {num}")

        except KeyError as e:
            print(f"Error: Missing field {e} in task data.")
        except TypeError as e:
            print(f"Error while counting completed tasks: {e}")

    def pending_tasks(self):
        try:
            num = 0
            for row in self.tasks:
                if row['completed'] is False:
                    num += 1
            print(f"The number of not completed tasks: {num}")

        except KeyError as e:
            print(f"Error: Missing field {e} in task data.")
        except TypeError as e:
            print(f"Error while counting pending tasks: {e}")

    def average_priority(self):
        try:
            if not self.tasks:
                print("Error: Cannot calculate average priority because there are no tasks.")
                return

            num = 0
            for row in self.tasks:
                num += int(row['priority'])

            res = num / len(self.tasks)
            print(f"The average priority level of all tasks: {res}")

        except KeyError as e:
            print(f"Error: Missing field {e} in task data.")
        except (TypeError, ValueError) as e:
            print(f"Error: Invalid priority value: {e}")
        except ZeroDivisionError:
            print("Error: Cannot divide by zero.")

    def save(self):
        try:
            with open("tasks.json", "wt") as file:
                json.dump(self.tasks, file, indent=2)
            print("Tasks successfully saved")

        except OSError as e:
            print(f"Error while saving tasks.json: {e}")
        except TypeError as e:
            print(f"Error: Data cannot be converted to JSON: {e}")

    def load(self):
        try:
            self.tasks = []

            with open("tasks.json", "rt") as file:
                reader = json.load(file)

            if not isinstance(reader, list):
                print("Error: tasks.json should contain a list of tasks.")
                return

            if not reader:
                print("Error: tasks.json is empty.")
                return

            for row in reader:
                if not isinstance(row, dict):
                    print("Error: Invalid task format in tasks.json.")
                    self.tasks = []
                    return

                required_fields = ["id", "task", "completed", "priority"]

                for field in required_fields:
                    if field not in row:
                        print(f"Error: Missing '{field}' field in tasks.json.")
                        self.tasks = []
                        return

                if not isinstance(row["id"], int):
                    print("Error: Task ID must be an integer.")
                    self.tasks = []
                    return

                if not isinstance(row["task"], str):
                    print("Error: Task name must be a string.")
                    self.tasks = []
                    return

                if not isinstance(row["completed"], bool):
                    print("Error: Completed must be True or False.")
                    self.tasks = []
                    return

                try:
                    int(row["priority"])
                except (TypeError, ValueError):
                    print("Error: Priority must be a number.")
                    self.tasks = []
                    return

                self.tasks.append(row)

            self.next_task_id = max(row["id"] for row in self.tasks) + 1
            print("Tasks successfully loaded!\n")

        except FileNotFoundError:
            print("Error: tasks.json file was not found.")
            print("Please create tasks.json first.")
        except json.JSONDecodeError:
            print("Error: tasks.json contains invalid JSON.")
        except PermissionError:
            print("Error: Permission denied while reading tasks.json.")
        except OSError as e:
            print(f"Error while reading tasks.json: {e}")
        except (KeyError, TypeError, ValueError) as e:
            print(f"Error: Invalid data in tasks.json: {e}")

    def convert_to_csv(self):
        try:
            if not self.tasks:
                print("Error: There are no tasks to convert.")
                return

            columns = ["ID", "Task Name", "Completed Status", "Priority"]

            with open("tasks.csv", "wt", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(columns)

                for task in self.tasks:
                    writer.writerow([
                        task["id"],
                        task["task"],
                        task["completed"],
                        task["priority"]
                    ])

            print("JSON file successfully converted to CSV file")

        except KeyError as e:
            print(f"Error: Missing field {e} in task data.")
        except PermissionError:
            print("Error: Permission denied while creating tasks.csv.")
        except OSError as e:
            print(f"Error while creating tasks.csv: {e}")
        except csv.Error as e:
            print(f"Error while writing CSV file: {e}")

    def run(self):
        self.load()

        while True:
            print("\n")
            print("1. Create a task\n2. Read tasks\n3. Update a task\n4. Delete a task\n5. Total tasks\n6. Completed tasks\n7. Pending tasks\n8. Average priority\n9. Save\n10. Load\n11. Convert to CSV file\n12. Exit")

            choice = input("Select: ")

            if choice not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]:
                print("Command Not Found")
                continue

            if choice == "12":
                print("Program exited.")
                break

            elif choice == "1":
                try:
                    task = input("Task name: ")
                    completed_input = input("Completed(True/False): ")
                    priority = int(input("Priority: "))
                    self.create(task, completed_input, priority)
                except ValueError:
                    print("Error: Priority must be a number.")

            elif choice == "2":
                self.read()

            elif choice == "3":
                try:
                    id = input("Task id for updating: ")
                    task = input("Updated name: ")
                    completed_input = input("Change a completed section(True/False): ")
                    priority_input = input("Updated priority: ")

                    if priority_input == "":
                        priority = None
                    else:
                        priority = int(priority_input)

                    self.update(id, task, completed_input, priority)

                except ValueError:
                    print("Error: Priority must be a number.")

            elif choice == "4":
                try:
                    id = input("Deleting ID: ")

                    if not id:
                        print("Error: ID cannot be empty.")
                        continue

                    self.delete(id)

                except ValueError:
                    print("Error: Invalid ID.")

            elif choice == "5":
                self.total_tasks()

            elif choice == "6":
                self.completed_tasks()

            elif choice == "7":
                self.pending_tasks()

            elif choice == "8":
                self.average_priority()

            elif choice == "9":
                self.save()

            elif choice == "10":
                self.load()

            elif choice == "11":
                self.convert_to_csv()


task_manager = Manager()
task_manager.run()
