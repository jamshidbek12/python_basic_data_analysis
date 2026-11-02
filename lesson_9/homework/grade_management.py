import csv

class CommanDNotFound(Exception):
    pass

class NotEnoughCredentials(Exception):
    pass

class FIleNotFoundError(Exception):
    pass

class Student:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject
        self.grade = 0

class Grade:
    def __init__(self):
        self.data = []
        self.averages = {}

    def grade(self, name, subject, grade):
        if not (name and subject and grade):
            raise NotEnoughCredentials("Not enough credentials")
        data = self.data
        student = Student(name, subject)
        student.grade = grade
        data.append({"Name": student.name, "Subject": student.subject, "Grade": student.grade})
        print(f"Student successfully graded")      

    def read(self):
        data = self.data
        if not data:
            print("Data not found\n")
            return
        
        for student in data:
            print(f"{student["Name"]}, {student["Subject"]}, {student["Grade"]}")
    def average_grades(self):
        data = self.data
        all_grades = {}
        for sub in data:
            subject = sub["Subject"]
            grade = float(sub["Grade"])
            if subject not in all_grades:
                all_grades[subject] = []
            all_grades[subject].append(grade)

        for subject in all_grades:
            grade_list = all_grades[subject]
            average = sum(grade_list) / len(grade_list)
            self.averages[subject] = average
            print(f"{subject}: {average}")
    def save(self):
        data = self.data
        if not data:
            print("Data not found")
            return
        columns = ["Name", "Subject", "Grade"]
        with open("grades.csv", mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(columns)
            writer.writerows([s["Name"], s["Subject"], s["Grade"]] for s in data)
        print("Data successfully saved!\n")

    def load(self):
        self.data = []
        try:
            with open("grades.csv", "rt") as file:
                reader = csv.reader(file)
                columns = next(reader)
                for row in reader:
                    self.data.append({"Name":row[0], "Subject":row[1], "Grade":row[2]})
                # print(reader)
        except FileNotFoundError:
            raise FIleNotFoundError("Error in file loading")
        print("Data successfully loaded")

    def save_averages(self):
        averages = self.averages
        if not averages:
            print("Data not found")
            return
        columns = ["Subject", "Average Grade"]
        with open("average_grades.csv", mode='wt', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(columns)
            writer.writerows([[k, v] for k, v in zip(averages.keys(), averages.values())])
        print("Average Grades successfully saved!")

    def load_averages(self):
        self.averages = {}
        try:
            with open("average_grades.csv", mode='rt') as file:
                reader = csv.reader(file)
                columns = next(reader)
                for row in reader:
                    self.averages[row[0]] = row[1]
        except FileNotFoundError:
            raise FIleNotFoundError("Error in file loading")
    def run(self):
        self.load()
        self.load_averages()
        while(True):
            print("\n")
            print(f"1. Grade a student\n2. Read\n3. Average grades\n4. Save\n5. Load\n6. Exit")
            choice = input("Select: ")
            try:
                if choice not in ["1","2","3","4","5","6",]:
                    raise CommanDNotFound(f"Command not found, with {choice}")

                if choice == "6":
                    break
                elif choice == "1":
                    name = input("Name: ")
                    subject = input("Subject: ")
                    grade = input("Grade: ")
                    self.grade(name, subject, grade)
                elif choice == "2":
                    self.read()
                elif choice == "3":
                    self.average_grades()
                elif choice == "4":
                    self.save()
                    self.save_averages()
                elif choice == "5":
                    self.load()
                    self.load_averages()
            except (CommanDNotFound, FileNotFoundError, NotEnoughCredentials) as e:
                print(f"Error: {e}\n")
grading_manager = Grade()
grading_manager.run()
            