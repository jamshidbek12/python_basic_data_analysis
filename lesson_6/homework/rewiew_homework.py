def check(func):
    def wrapper(a,b):
        try:
            ans = a / b
        except ZeroDivisionError:
            return("Denominator can't be zero")
        else:
            return ans
    return wrapper

@check
def div(a, b):
    return a / b

num_zero1 = int(input())
num_zero2 = int(input())

print(div(num_zero1, num_zero2))


def append(user):
    with open("employees.txt", "a") as f:
        f.write(user)
        print(f"Successfully added: {user}")

def read():
    with open("employees.txt", "rt") as f:
        content = f.read()
        return content if content else "No records found\n"

def search_by_id(id):
    with open("employees.txt") as f:
        for x in f.readlines():
            if x.split(",")[0].strip() == str(id):
                return x
    return "User not found\n"

def delete_by_id(id):
    with open("employees.txt") as f:
        lines = f.readlines()
    found = False
    with open("employees.txt", "w") as f:
        for line in lines:
            if line.split(",")[0].strip() != str(id):
                f.write(line)
            else:
                found = True
    print("Successfully Deleted\n" if found else "User not found\n")

def update_by_id(id, new_name=None, new_position=None, new_salary=None):
    with open("employees.txt") as f:
        lines = f.readlines()
    updated = False
    with open("employees.txt", "w") as f:
        for line in lines:
            parts = line.strip().split(",")
            emp_id = parts[0].strip()

            if emp_id == str(id):
                name = new_name if new_name else parts[1].strip()
                position = new_position if new_position else parts[2].strip()
                salary = new_salary if new_salary else parts[3].strip()

                new_line = f"{emp_id}, {name}, {position}, {salary}\n"
                f.write(new_line)
                updated = True
            else:
                f.write(line)
    print("Successfully updated\n" if updated else "User not found\n")

while True:
    print("1. Add\n2. View\n3. Search\n4. Update\n5. Delete\n6. Exit")
    choice = input("Select: ",)
    print("\n")
    if choice == "6":
        break
    elif choice == "1":
        id = str(input("ID: "))
        name = str(input("Name: "))
        position = str(input("Position: "))
        salary = input("Salary: ")
        user = f"{id}, {name}, {position}, {salary}\n"
        append(user)

    elif choice == "2":
        print(read())
    elif choice == "3":
        id = input("Searching ID: ")
        print(search_by_id(id))
    elif choice == "4":
        id = str(input("ID: "))
        name = str(input("Name (Leave blank if you are not making changes): "))
        position = str(input("Position: (Leave blank if you are not making changes)"))
        salary = input("Salary: (Leave blank if you are not making changes)")
        update_by_id(id, new_name=name, new_position=position, new_salary=salary)
    elif choice == "5":
        id = input("Deleting ID: ")
        delete_by_id(id)

import os
import string
from collections import Counter

if os.path.exists("sample.txt"):
    pass
else: 
    with open("sample.txt", "wt") as f:
        text = input("Could you write some text?: ")
        f.write(text)

with open("sample.txt") as f:
    text = f.read()
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    words = text.split()
    word_counts = Counter(words)
    top_5 = word_counts.most_common(5)
    len_text = len(words)
    print(f"Total words: {len_text}")
    print(f"Top 5 most common words:")
    for word, count in top_5:
        print(f"{word} - {count} times")

with open("word_count_report.txt", "w") as f:
    f.write("Word Count Report\n")
    f.write(f"Total Words: {len_text}\n")
    f.write("Top 5 Words:\n")
    for word, count in top_5:
        f.write(f"{word} - {count}\n")