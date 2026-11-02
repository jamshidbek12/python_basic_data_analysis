# List Tasks

# 1
list1 = [1,1,2,3,4,5,6,4,5,1,2,5]
print(list1.count(5))

# 2
list2 = [1,1,2,5,1,2,5]
print(sum(list2))

# 3
list3 = [3,3,7,5,1,2,5]
print(max(list3))

# 4
list4 = [3,3,7,5,1,2,5]
print(min(list4))

# 5
list5 = [3,3,7,5,1,2,5]
print(5 in list5)  

# 6
list6 = [3,4,7,5,1,2,5]
print(list6[0] if list6 else None)

# 7
list7 = [3,4,7,5,1,2,5]
print(list7[-1] if list7 else None)

# 8
list8 = [3,5,1,2,5]
new_list8 = list8[:3]
print(new_list8)

# 9
list9 = [3,5,1,2,5]
new_list9 = list9[::-1]
print(new_list9)

# 10
list10 = [4,7,2,5,7,5,4,9]
new_list10 = list10.copy()
new_list10.sort()
print(new_list10)

# 11
original_list11 = [4,7,2,5,7,5,4,9,2]
new_set_list11 = set(original_list11)
list11 = list(new_set_list11)
print(list11)

# 12
list12 = [7,5,4,9,2]
list12.insert(1,7)
print(list12)

# 13
list13 = [7,5,4,9,2]
if 7 in list13:
    print(list13.index(7))
else:
    print("Element not found")

# 14
lst14 = []
print(len(lst14) == 0)

# 15
list15 = [4,7,6,8,9,2,4,5,6]
even15 = 0
for i in list15:
    if i%2==0:
        even15 += 1
print(even15)

# 16
list16 = [4,7,6,8,9,2,4,5,6]
not_even16 = 0
for i in list16:
    if i%2!=0:
        not_even16 += 1
print(not_even16)

# 17
list17_1 = [2,4,5,6]
list17_2 = [2,4,5,6]
list17_3 = list17_1+list17_2
print(list17_3)

# 18
list18 = [1, 2, 3, 4, 5, 8, 9, 6, 5]
sub_list18 = [2, 3, 4]
checking18 = all(x in list18 for x in sub_list18)
print(checking18)

# 19
list19 = [1, 6, 5, 4, 6, 7]
pos19 = list19.index(5)
list19[pos19] = 77
print(list19)

# 20
list20 = [1, 8, 5, 8, 4, 6, 7]
set_list20 = set(list20)
new_list20 = list(set_list20)
new_list20.sort(reverse=True)
print(new_list20[1])

# 21
list21 = [1, 8, 5, 8, 4, 6, 7]
set_list21 = set(list21)
new_list21 = list(set_list21)
new_list21.sort()
print(new_list21[1])

# 22
list22 = [4,7,6,8,9,2,4,5,6]
even22 = []
for i in list22:
    if i%2==0:
        even22.append(i)
print(even22)

# 23
list23 = [4,7,6,8,9,2,4,5,6]
odd23 = []
for i in list23:
    if i%2!=0:
        odd23.append(i)
print(odd23)

# 24
list24 = [3,5,6,3,4,5]
print(len(list24))

# 25
original_list24 = [3,5,6,3,4,5]
copy_list25 = original_list24.copy()
print(copy_list25)

# 26
list26 = [3,5,4,3,4,5,9,1]
len_list26 = len(list26)

if len_list26 % 2 == 0:
    index26 = int(len_list26/2)
    print(list26[index26-1])
    print(list26[index26])
else:
    index26 = int((len_list26+1)/2)
    print(list26[index26-1])

# 27
list27 = [3,6,8,5,4,6,3,1,8,9]
sublist27 = list27[3:8]
print(max(sublist27))

# 28
list28 = [3,6,8,5,4,6,3,1,8,9]
sublist28 = list28[3:8]
print(min(sublist28))

# 29
list29 = [3,6,8,8,9]
index29 = 4

if len(list29) > index29 >=0:
    list29.pop(index29)
    print("Successfully deleted")
else:
    print("Index not found")

# 30
list30 = [1,2,3,4,5,6,7]
print("YES") if sorted(list30) == list30 else print("NO")

# 31
list31 = [4,5,6,7]
given_n31 = 3
new_list31 = []

for i in list31:
    new_list31 += [i] * given_n31

print(new_list31)

# 32
list32_1 = [4,5,6,7]
list32_2 = [4,5,6,7]
new_list32 = list32_1 + list32_2
new_list32.sort()
print(new_list32)

# 33
list33 = [4,5,4,7,4]
given_elm = 4
new_list33 = []

for i in range(len(list33)):
    if list33[i] == given_elm:
        new_list33.append(i)
print(new_list33)

# 34
list34 = [4,6,8,7,6,3]
last_elm34 = list34[-1:]
others34 = list34[:-1]
new_list34 = last_elm34+others34
print(new_list34)

# 35
number35 = range(1,11)
list35 = list(number35)
print(list35)

# 36
list36 = [7,5,6,-9,-6,-3,-6,5,4]
new_list36 = 0

for i in list36:
    if i>0:
        new_list36+=i
print(new_list36)

# 37
list37 = [7,5,6,-9,-6,-3,-6,5,4]
new_list37 = 0

for i in list37:
    if i<0:
        new_list37+=i  
print(new_list37)
    
# 38
list38 = [1,2,3,3,2,1,]
print("Palindrome") if list38[::-1] == list38 else print("Not palindrome")

# 39
user39_1 = [0,0,0,2,3,6]
user39_2 = [0,0,0,1,4,7]
users39 = [user39_1,user39_2]
print(users39)

# 40
list40 = [0,0,2,3,6,2,6,5,4,3]
set40 = set(list40)
new_list40 = list(set40)
print(new_list40)

# Tuple tasks
# 1
tup1 = (3,4,5,2,3,5,6)
print(tup1.count(3))

# 2
tup2 = (3,4,5,6,7,5,3,2)
print(max(tup2))

# 3
tup3 = (3,4,5,6,7,5,3,2)
print(min(tup3))

# 4
tup4 = (3,4,5,6,7,5,3,2)
element4 = 4
print(True) if element4 in tup4 else print(False)

# 5
tup5 = (3,4,5,6,7,5,3,2)
print("None") if len(tup5)==0 else print(tup5[0])

# 6
tup6 = (3,4,5,6,7,5,3,2)
print("None") if len(tup6)==0 else print(tup6[-1])

# 7
tup7 = (3,4,5,6,7,5,3,2)
print(len(tup7))

# 8
tup8 = (3,4,5,6,7,5,3,2)
print(tup8[:3])

# 9
tup9_1 = (3,4,5,6,7,5,3,2)
tup9_2 = (5,3,2,5,3,)
new_tup9 = tup9_1 + tup9_2
print(new_tup9)

# 10
tup10 = (3,4,5,6,7,5,3,2)
print(None) if len(tup10)==0 else print("Not empty")

# 11
tup11 = (3,4,5,3,6,7,5,3,2)
given_elem11 = 3
ans11 = []
for i in range(len(tup11)):
    if tup11[i] == given_elem11:
        ans11.append(i)
print(ans11)

# 12
tup12 = (3,4,5,3,6,7,5,3,2)
print(sorted(tup12, reverse=True)[1])

# 13
tup13 = (3,4,5,3,6,7,5,3,2)
print(sorted(tup13)[1])

# 14
tup14 = (7,)
print(tup14)

# 15
tup_list15 = [2,3,5,4]
tup15 = tuple(tup_list15.copy())
print(tup15)

# 16
tup16 = (1,2,3,4,5,6,7)
print(True) if tup16 == tuple(sorted(tup16)) else print(False)

# 17
tup17 = (1,2,3,4,5,6,7)
subtup17 = tup16[2:6]
print(max(subtup17))

# 18
tup18 = (1,2,3,4,5,6,7)
subtup18 = tup18[2:6]
print(min(subtup18))

# 19
tpl19 = (1, 2, 3, 2, 4)
lst19tpl = list(tpl19)
lst19tpl.remove(2)
print(tuple(lst19tpl))

# 20
original_tuple20 = (1,2,3,4,5,6,7)
tpl20 = []
chunk_size20 = 2

for i in range(0,len(original_tuple20),chunk_size20):
    ans20 = (original_tuple20[i: i+chunk_size20])
    tpl20.append(ans20)
print(tuple(tpl20))

# 21
tpl21 = (2,3,4,5,6,7)
gv_nm21 = 3
tpl_list_21 = []

for i in tpl21:
    tpl_list_21+=((i,) * gv_nm21)
print(tuple(tpl_list_21))

# 22
tpl22 = tuple(range(1,11))
print(tpl22)

# 23
tpl23 = (3,4,5,6,7,8)
new_tpl23 = tpl23[::-1]
print(new_tpl23)

# 24
tpl24 = (1,2,3,3,2,1)
print("Palindrome") if tpl24 == tpl24[::-1] else print("Not palindrome")

# 25
tpl25 = (1,2,3,3,2,1)
tpl_list25 = [] 

for i in tpl25:
    if i not in tpl_list25:
        tpl_list25.append(i)
print(tuple(tpl_list25))

# Set Tasks
# 1
st1_1 = {1,2,3,3}
st1_2 = {3,4,5}
new_st1 = st1_1 | st1_2
print(new_st1)

# 2
st2_1 = {1,2,3,3}
st2_2 = {3,4,5}
new_st2 = st2_1 & st2_2
print(new_st2)

# 3
st3_1 = {1,2,3}
st3_2 = {3,4,5}
new_st3 = st3_1 - st3_2
print(new_st3)

# 4
st4_1 = {1,2,3}
st4_2 = {1,2,3,4,5,6,7}
new_st4 = st4_1 <= st4_2
print(new_st4)

# 5
st5 = {1,2,3,5,6,7}
st5_elm = 4
print(True) if st5_elm in st5 else print(False)

# 6
st6 = {1,2,3,5,6,7}
print(len(st6))

# 7
st7_list = [1,2,3,4,4,3,2,2,3]
st7 = set(st7_list)
print(st7)

# 8
st8 = {1,2,3,4,4,3,2,2,3}
st8_elem = 4
if st8_elem in st8:
    st8.remove(st8_elem)
    print(st8)
else:
    print(None)


# 9
st9 = {4,6,8,9,5}
new_st9 = st9.copy()
new_st9.clear()
print(new_st9)

# 10
st10 = {4,6,8,9,5}
print("Empty") if len(st10)==0 else print("Not empty")

# 11
st11_1 = {1,2,3}
st11_2 = {3,4,5}
new_st11 = st11_1 ^ st11_2
print(new_st11)

# 12
st12 = {1,2,3,4}
st12_elm = 4
st12.add(st12_elm)
print(st12)

# 13
st13 = {5,2,3,4,6,4,5,6,5}
popped_elm13 = st13.pop()
print(popped_elm13)
print(st13)

# 14
st14 = {8,7,3,5,6,4,8,9}
print(max(st14))

# 15
st15 = {8,7,3,5,6,4,8,9}
print(min(st15))

# 16
st16 = {8,7,3,5,6,4,9}
even_st16 = []

for i in st16:
    if i%2 == 0:
        even_st16.append(i)
print(set(even_st16))

# 17
st17 = {8,7,3,5,6,4,9}
even_st17 = []

for i in st17:
    if i%2 != 0:
        even_st17.append(i)
print(set(even_st17))

# 18
st18 = set(range(1,11))
print(st18)

# 19
st19_1 = {1,2,3,4,5}
st19_2 = {4,5,6,7,8}
new_st19 = st19_1 | st19_2
print(new_st19)

# 20
st20_1 = {1,2,3,4,5}
st20_2 = {4,5,6,7,8}
new_st20 = st20_1.isdisjoint(st20_2)
print(new_st20)

# 21
st21_list = [1,2,3,4,55,4,3,2,3]
st21 =  set(st21_list)
print(list(st21))

# 22
st22_list = [1,2,3,4,55,4,3,2,3]
st22 =  set(st22_list)
print(len(st22))

# 23
import random
st23 = set()
st23_i = 0

st23_spec_num = 5

while len(st23)<5:
    st23_ran = random.randint(1,100)
    st23.add(st23_ran)
    st23_i+=1
print(st23)

# Dictionary Tasks]
# 1
dct1 = {
    "model": "Ford",
    "year": 2024,
    "user": "John"
}
key1 = "model"
res1 = dct1.get(key1, "Not found")
print(res1)

# 2
dct2 = {
    "model": "Ford",
    "year": 2024,
    "user": "John"
}
key2 = "model"
print(True) if key2 in dct2 else print(False)

# 3
dct3 = {
    "model": "Ford",
    "year": 2024,
    "user": "John"
}
print(len(dct3.keys()))

# 4
dct4 = {
    "model": "Ford",
    "year": 2024,
    "user": "John"
}
dct4_list = list(dct4.keys())
print(dct4_list)

# 5
dct5 = {
    "model": "Ford",
    "year": 2024,
    "user": "John"
}
dct5_list = list(dct5.values())
print(dct5_list)

# 6
dct6_1 = {
    "model": "Ford",
    "year": 2024,
    "user": "John"
}

dct6_2 = {
    "city": "Tashkent",
    "job": "Developer",
    "year": 2020
}
new_dct6 = dct6_1.copy()
new_dct6.update(dct6_2)
print(new_dct6)

# 7
dct7 = {
    "model": "Ford", "year": 2024, "user": "John"
}
dct7_key = "user"
print(dct7.pop(dct7_key, "Not Found"))

# 8
dct8 = {
    "model": "Ford", "year": 2024, "user": "John"
}
new_dct8 = dct8.copy()
new_dct8.clear()
print(new_dct8)

# 9
dct9 = {"model": "Ford", "year": 2024, "user": "John"}
print("Empty") if len(dct9)==0 else print("Not Empty")

# 10
dct10 = {"model": "Ford", "year": 2024, "user": "John"}
dct10_key = "model"

if dct10_key in dct10:
    dct10_tpl = (dct10_key, dct10.get(dct10_key))
    print(dct10_tpl)
else:
    print("Not Found")

# 11
dct11 = {"model": "Ford", "year": 2024, "user": "John"}
dct11_key = "model"
dct11.update({dct11_key: "Mustang"})
print(dct11)

# 12
dct12 = {"a": 5, "b": 3, "c": 5, "d": 5, "e": 2}
dct12_value = 5
dct12_ans = list(dct12.values()).count(dct12_value)
print(dct12_ans)

# 13
dct13 = {"a": 1, "b": 2, "c": 3}
new_dct13 = {}

for key,value in dct13.items():
    new_dct13.update({value:key})
print(new_dct13)

# 14
dct14 = {"a": 5, "b": 3, "c": 5, "d": 5, "e": 2}
dct14_value = 5
dct14_list = []
for key, value in dct14.items():
    if value == dct14_value:
        dct14_list.append(key)
print(dct14_list)

# 15
dct15_val = ["a", "b", "c"]
dct15_key = [1, 2, 3]
print(dict(zip(dct15_key, dct15_val)))

# 16
dct16 = {"a": 1, "b": {"name":"Hons", "age":12}, "c": 3}
dct16_ans = []
for value in dct16.values():
    if isinstance(value, dict):
        dct16_ans.append(True)
    else:
        dct16_ans.append(False)
print(any(dct16_ans))

# 17
dct17 = {"a": 1, "b": {"name":"Hons", "age":12}, "c": 3}
print(dct17["b"]["name"])

# 18
dict18 = {"a": 1, "b": 2}
dict18_x = dict18.setdefault("c", 3)
print(dict18)

# 19
dict19 = {"a": 5, "b": 3, "c": 5, "d": 5, "e": 2}
print(len(set(dict19.values())))

# 20
dict20 = {"d": 5, "c": 3, "d": 4, "a": 1, "b": 2}
print(dict(sorted(dict20.items())))

# 21
dict21 = {'a': 3, 'b': 1, 'c': 2}
print(dict(sorted(dict21.items(), key=lambda x: x[1])))

# 22
dct22 = {"a": 8, "b": 3, "c": 7, "d": 9, "e": 2}
dct22_ans = {}
for key, value in dct22.items():
    if value > 5:
        dct22_ans[key] = value
print(dct22_ans)

# 23
dct23_1 = {"a": 1, "b": 2, "c": 3}
dct23_2 = {"c": 10, "d": 20}
print(True) if dct23_1.keys() & dct23_2.keys() else print(False)

# 24
dct24_tpl = (("a", 1), ("b", 2), ("c", 3))
print(dict(dct24_tpl))

# 25
dct25 = {'a': 3, 'b': 1, 'c': 2}
print(list(dct25.items())[0])
