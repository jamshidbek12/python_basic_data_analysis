# Number Data Type Questions:
# 1
n_1 = float(input())
print(round(n_1, 2))

# 2
a_2 = float(input())
b_2 = float(input())
c_2 = float(input())

print(max(a_2, b_2, c_2))
print(min(a_2, b_2, c_2))

# 3
km_3 = float(input())

if km_3 <= 0:
    print('0')
else:
    m_3 = km_3 * 1000
    cm_3 = m_3 * 100
    print(f"Meters: {m_3}")
    print(f"Centimeters: {cm_3}")

# 4
s_4 = input()

cleaned = ""
for char in s_4:
    if char.isalnum():
        cleaned += char.lower()

if cleaned[::-1] == cleaned:
    print("Palindrome")
else:
    print("Not palindrome")

# 5
s_5 = input()
l_s_5 = s_5.lower()

list_v_5 = ["a", "e", "i", "o", "u"]

vowels = 0
consonants = 0

for char in l_s_5:
    if char in list_v_5:
        vowels +=1
    elif char.isalpha():
        consonants +=1

print(f"Vowels: {vowels}")
print(f"Consonants: {consonants}")

# 6
s_6 = input()
sec_6 = input()

print(sec_6 in s_6)

# 7
s_7 = input("Input sentence: ")
replace_s_7 = input("Replace: ")
with_s_7 = input("With: ")

result_7 = s_7.replace(replace_s_7, with_s_7) 

print(f"Output: {result_7}")

# 8
s_8 = input()
print(s_8[0])
print(s_8[-1])

# 9
s_9 = input()
result_9 = s_9[::-1]
print(result_9)

# 10    
s_10 = input()
counts = 0

second_s = s_10.split(" ")
for i in range(len(second_s)):
    counts+= len(second_s[i])

print(counts)

# 11
s_11 = input()

has_digits_11 = False

for i in range(len(s_11)):
    if s_11[i].isnumeric():
        has_digits_11 = True

print(has_digits_11)

# 12
s_12 = input()

split_12 = s_12.split(" ")
res_12 = "-".join(split_12)
print(res_12)

# 13
s_13 = input()

split_13 = s_13.split(" ")
res_13 = "".join(split_13)
print(res_13)

# 14
a_14 = input()
b_14 = input()

if a_14 == b_14 :
    print("Equal")
else: 
    print("Not equal")

# 15
s_15 = input()

split_15 = s_15.split()
list_15 = []

for i in range(len(split_15)):
    list_15.append(split_15[i][0])

res_15 = "".join(list_15)
print(res_15)

# 16
s_16 = input()
char_16 = input()

split_16 = s_16.split(char_16)
res_16 = "".join(split_16)
print(res_16)

# 17
s_17 = input()

split_17 = s_17.split(" ")
print(f"Input: \"{s_17}\"")
print(f"Starts with: \"{split_17[0]}\"")
print(f"Ends with: \"{split_17[-1]}\"")

# Boolean Data Type Questions:
# 1
user_1 = input()
password_1 = input()

if user_1 and password_1:
    print(True)
else:
    print(False)

# 2
n_1_2 = int(input())
n_2_2 = int(input())

if n_1_2 == n_2_2:
    print("Equal")
else:
    print("Not equal")

# 3
n_1_b = int(input())

if n_1_b>0 and (n_1_b%2==0):
    print(True)
else:
    print(False)

# 4
n_1_2 = int(input())
n_2_2 = int(input())
n_3_2 = int(input())

if (n_1_2 == n_2_2) or (n_1_2 == n_3_2) or((n_2_2 == n_3_2)):
    print("Not different")
else:
    print("Different")

# 5
s_51_b = input()
s_52_b = input()

if len(s_51_b) == len(s_52_b):
    print(True)
else:
    print(False)

# 6
n_6_b = int(input())

if (n_6_b%5==0) and (n_6_b%3==0):
    print(True)
else:
    print(False)

# 7
n_7_b1 = int(input())
n_7_b2 = int(input())

if (n_7_b1+n_7_b2)>50:
    print(True)
else:
    print(False)

# 8
n_8_b = int(input())

if (n_8_b>=10) and (n_8_b<=20) :
    print(True)
else:
    print(False)









