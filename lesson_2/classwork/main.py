## Number Data Type Questions:
# 1
fl_num = float(input())
print(round(fl_num, 2))

# 2
a_sec = int(input()) 
b_sec = int(input()) 
c_sec = int(input())

minimum = min(a_sec, b_sec, c_sec) 
maximum = max(a_sec, b_sec, c_sec) 
print(maximum, minimum)

# 3
km = float(input())

meters = km * 1000
centimeters = km * 100000

print(meters)
print(centimeters)

# 4
four_a = int(input())
four_b = int(input())
# 
# print(divmod(four_a, four_b))
print(four_a // four_b, four_a % four_b)

# 5
celsius = float(input())

f = (celsius * 9/5) + 32

print(f)

# 6
num = int(input("Enter a number: "))

last_digit = abs(num) % 10

print(last_digit)

# 7
s_a = int(input())

if s_a % 2 == 0:
    print("even")
else:
    print("odd")

#  Strings
# 1
fs_name = input()
fs_date = int(input())

print(2026 - fs_date)

# 2
scs_txt = 'LMaasleitbtui'

car1 = scs_txt[0::2]  
car2 = scs_txt[1::2]  # M, a, l, i, b, i

print(car1)  # Lasetu
print(car2)  # Malibi

# 3
ths_string = input()

ths_length = len(ths_string)

upper = ths_string.upper()
lower = ths_string.lower()

print(ths_length)
print(upper)
print(lower)

# 4
s = input().lower()
print(s==s[::-1])

# 5
fvs_s = input()
unli_harflar = ['a','e','i','o','u']
unli_c = 0
undosh_c =0
for i in range(len(fvs_s)):
    if fvs_s[i].lower() in unli_harflar:
        unli_c+=1
    else:
        undosh_c+=1
print(unli_c)
print(undosh_c)

# 6
sxs_text = input()
sxs_search = input()

if sxs_search in sxs_text:
    print(True);
else:
    print(False);

# 7
sevs_text = input();
sevs_old_world = input();
sevs_new_world = input();

sevs_result = sevs_text.replace(sevs_old_world, sevs_new_world);
print(sevs_result)

# 8
egs_text = input()
print(egs_text[0], egs_text[-1])

# 9
ngs_text = input();
reversed_text = ngs_text[::-1]
print(reversed_text)

# 10
tens_text = input();
length_text = len(tens_text);
print(length_text)


# 11
els_text = input();

if any(char.isdigit() for char in els_text):
    print(True);
else:
    print(False);

# 12
tws_words = input()
tws_separator = '-'

word_list = tws_words.split()
tws_result = tws_separator.join(word_list)

print(tws_result)

# 13
tthr_text = input();
tthr_result = tthr_text.split();
print("".join(tthr_result))

# 14
tfr_text_1 = input()
tfr_text_2 = input()
if tfr_text_1 == tfr_text_2:
    print(True);
else: 
    print(False);

# 15
tfv_text = input()

tfv_acronym = "".join(world[0].upper() for world in tfv_text.split())

print(tfv_acronym)

# 16
tscs_text = input();
tscs_char = input();

tscs_result = tscs_text.replace(tscs_char, "");
print(tscs_result);

# 17
tsvn_text = input();
tsvn_result = "";
tsvn_unlilar = ['a','e','i','o','u'];

for i in range(len(tsvn_text)):
    if tsvn_text[i].lower() in tsvn_unlilar: 
        tsvn_result+="*";
    else: 
        tsvn_result+= tsvn_text[i];
print(tsvn_result)

# 18
tegh_text = input();
tegh_massiv = tegh_text.split();
print(tegh_massiv[0])
print(tegh_massiv[-1])


## BOOLEAN ###
# 1
username = input()
password = input()

if username and password:
    print("Username and password are valid")
else:
    if not username:
        print("Username cannot be empty")
    if not password:
        print("Password cannot be empty")

# 2
t2_num1 = float(input())
t2_num2 = float(input())

if t2_num1 == t2_num2:
    print(f"{t2_num1} and {t2_num2} are equal")
else:
    print(f"{t2_num1} and {t2_num2} are not equal")

# 3
t3_num = int(input())

if t3_num > 0 and t3_num % 2 == 0:
    print(f"{t3_num} is positive and even")
elif t3_num > 0 and t3_num % 2 != 0:
    print(f"{t3_num} is positive and odd")
elif t3_num < 0 and t3_num % 2 == 0:
    print(f"{t3_num} is negative and even")
elif t3_num < 0 and t3_num % 2 != 0:
    print(f"{t3_num} is negative and odd")
else:
    print(f"{t3_num} is zero")

# 4
t4_num1 = int(input())
t4_num2 = int(input())
t4_num3 = int(input())

if t4_num1 != t4_num2 and t4_num2 != t4_num3 and t4_num1 != t4_num3:
    print("All three numbers are different")
else:
    print("Some numbers are equal")

# 5
t5_text1 = input()
t5_text2 = input()

if len(t5_text1) == len(t5_text2):
    print("Both texts are the same length")
else:
    print("Texts have different lengths")

# # 6
t6_num = int(input())

if t6_num % 3 == 0 and t6_num % 5 == 0:
    print(f"{t6_num} is divisible by both 3 and 5")
elif t6_num % 3 == 0:
    print(f"{t6_num} is divisible by 3 only")
elif t6_num % 5 == 0:
    print(f"{t6_num} is divisible by 5 only")
else:
    print(f"{t6_num} is not divisible by 3 or 5")

# # 7
t7_num1 = int(input())
t7_num2 = int(input())

if t7_num1 + t7_num2 > 50:
    print("greater than > 50 ✓")
else:
    print("less than 50 ✗")

# 8
t8_num = int(input())

if 10 <= t8_num <= 20:
    print(f"{t8_num} is between 10 and 20")
else:
    print(f"{t8_num} is not between 10 and 20")