# Task 1
def convert_cel_to_far(c):
    return round(c*(9/5) + 32, 2)

def convert_far_to_cel(f):
    return round((f-32)*5/9, 2)

fah_1 = float(input("Enter a temperature in degrees F: "))
print(f"{fah_1:g} degrees F = {convert_far_to_cel(fah_1):.2f} degrees C")
print()
cel_1 = float(input("Enter a temperature in degrees C: "))
print(f"{cel_1:g} degrees C = {convert_cel_to_far(cel_1):.2f} degrees F")

# Task 2
def invest(amount, rate, years):
    old_amount = amount

    for i in range(1, years+1):
        new_amount = old_amount*(rate+1)
        old_amount = new_amount
        print(f"year {i} : ${new_amount:.2f}")

amount = float(input("Amount: "))
rate = float(input("Rate: "))
years = int(input("Years: "))
invest(amount, rate, years)

# Task 3
def check_fact(int_fact):
    i = 1
    while i<=int_fact:
        if int_fact % i ==0:
            print(f"{i} is a factor of {int_fact}")
        i+=1


int_fact = int(input("Enter a positive integer: "))
check_fact(int_fact)


# Task 4
universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]


def enrollment_stats(universities):
    list_students = []
    list_fees = []

    for i in universities:
        list_students.append(i[1])
        list_fees.append(i[2])
    return list_students, list_fees


def mean(values):
    result = sum(values) / len(values)
    return result


def median(values):
    sorted_values = sorted(values)
    n = len(sorted_values)

    if n % 2 == 0:
        mid1 = sorted_values[n // 2 - 1]
        mid2 = sorted_values[n // 2]
        return (mid1 + mid2) / 2
    else:
        return sorted_values[n // 2]


# Main part
list_students, list_tuition = enrollment_stats(universities)

total_students = sum(list_students)
total_tuition = sum(list_tuition)

student_mean = mean(list_students)
student_median = median(list_students)

tuition_mean = mean(list_tuition)
tuition_median = median(list_tuition)

print("*" * 30)
print(f"Total students: {total_students:,}")
print(f"Total tuition: $ {total_tuition:,}")
print()
print(f"Student mean: {student_mean:,.2f}")
print(f"Student median: {student_median:,}")
print()
print(f"Tuition mean: $ {tuition_mean:,.2f}")
print(f"Tuition median: $ {tuition_median:,}")
print("*" * 30)

# 5
def check_prime_num(num):
    if num <= 2:
        return False
    if num%2 == 0:
        return False
    i = 3
    while i*i<=num:
        if num%i == 0:
            return False
        i+=2
    return True

number = int(input())
check_prime_num(number)