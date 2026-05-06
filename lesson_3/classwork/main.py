# LIST

# 1
lst1 = [1, 2, 3, 2, 4, 2]
print(lst1.count(2))

# 2
lst2 = [1, 2, 3, 4, 5]
print(sum(lst2))

# 3
lst3 = [1, 2, 3, 4, 5]
print(max(lst3))

# 4
lst4 = [1, 2, 3, 4, 5]
print(min(lst4))

# 5
lst5 = [1, 2, 3, 4, 5]
print(3 in lst5)

# 6
lst6 = [1, 2, 3]
print(lst6[0] if lst6 else None)

# 7
lst7 = [1, 2, 3]
print(lst7[-1] if lst7 else None)

# 8
lst8 = [1, 2, 3, 4, 5]
print(lst8[:3])

# 9
lst9 = [1, 2, 3, 4, 5]
print(lst9[::-1])

# 10
lst10 = [3, 1, 4, 1, 5]
print(sorted(lst10))

# 11
lst11 = [1, 2, 2, 3, 3, 4]
print(list(set(lst11)))

# 12
lst12 = [1, 2, 3, 4]
lst12.insert(2, 99)
print(lst12)

# 13
lst13 = [1, 2, 3, 4]
print(lst13.index(3))

# 14
lst14 = []
print(len(lst14) == 0)

# 15
lst15 = [1, 2, 3, 4, 5, 6]
print(len([x for x in lst15 if x % 2 == 0]))

# 16
lst16 = [1, 2, 3, 4, 5, 6]
print(len([x for x in lst16 if x % 2 != 0]))

# 17
lst17a = [1, 2, 3]
lst17b = [4, 5, 6]
print(lst17a + lst17b)

# 18
lst18 = [1, 2, 3, 4, 5]
sublist18 = [2, 3, 4]
print(all(x in lst18 for x in sublist18))

# 19
lst19 = [1, 2, 3, 2, 4]
lst19[lst19.index(2)] = 99
print(lst19)

# 20
lst20 = [1, 2, 3, 4, 5]
print(sorted(set(lst20))[-2])

# 21
lst21 = [1, 2, 3, 4, 5]
print(sorted(set(lst21))[1])

# 22
lst22 = [1, 2, 3, 4, 5, 6]
print([x for x in lst22 if x % 2 == 0])

# 23
lst23 = [1, 2, 3, 4, 5, 6]
print([x for x in lst23 if x % 2 != 0])

# 24
lst24 = [1, 2, 3, 4, 5]
print(len(lst24))

# 25
lst25 = [1, 2, 3]
copy25 = lst25.copy()
print(copy25)

# 26
lst26 = [1, 2, 3, 4, 5]
mid26 = len(lst26) // 2
print(lst26[mid26] if len(lst26) % 2 != 0 else lst26[mid26-1:mid26+1])

# 27
lst27 = [1, 2, 3, 4, 5]
print(max(lst27[1:4]))

# 28
lst28 = [1, 2, 3, 4, 5]
print(min(lst28[1:4]))

# 29
lst29 = [1, 2, 3, 4, 5]
index29 = 2
if index29 < len(lst29):
    lst29.pop(index29)
print(lst29)

# 30
lst30 = [1, 2, 3, 4, 5]
print(lst30 == sorted(lst30))

# 31
lst31 = [1, 2, 3]
n31 = 2
print([x for x in lst31 for _ in range(n31)])

# 32
lst32a = [3, 1, 5]
lst32b = [4, 2, 6]
print(sorted(lst32a + lst32b))

# 33
lst33 = [1, 2, 3, 2, 4, 2]
print([i for i, x in enumerate(lst33) if x == 2])

# 34
lst34 = [1, 2, 3, 4, 5]
print(lst34[-1:] + lst34[:-1])

# 35
lst35 = list(range(1, 11))
print(lst35)

# 36
lst36 = [-1, 2, -3, 4, 5]
print(sum(x for x in lst36 if x > 0))

# 37
lst37 = [-1, 2, -3, 4, 5]
print(sum(x for x in lst37 if x < 0))

# 38
lst38 = [1, 2, 3, 2, 1]
print(lst38 == lst38[::-1])



# TUPLE

# 1
tpl1 = (1, 2, 3, 2, 4, 2)
print(tpl1.count(2))

# 2
tpl2 = (1, 2, 3, 4, 5)
print(max(tpl2))

# 3
tpl3 = (1, 2, 3, 4, 5)
print(min(tpl3))

# 4
tpl4 = (1, 2, 3, 4, 5)
print(3 in tpl4)

# 5
tpl5 = (1, 2, 3)
print(tpl5[0] if tpl5 else None)

# 6
tpl6 = (1, 2, 3)
print(tpl6[-1] if tpl6 else None)

# 7
tpl7 = (1, 2, 3, 4, 5)
print(len(tpl7))

# 8
tpl8 = (1, 2, 3, 4, 5)
print(tpl8[:3])

# 9
tpl9a = (1, 2, 3)
tpl9b = (4, 5, 6)
print(tpl9a + tpl9b)

# 10
tpl10 = ()
print(len(tpl10) == 0)

# 11
tpl11 = (1, 2, 3, 2, 4, 2)
print([i for i, x in enumerate(tpl11) if x == 2])

# 12
tpl12 = (1, 2, 3, 4, 5)
print(sorted(set(tpl12))[-2])

# 13
tpl13 = (1, 2, 3, 4, 5)
print(sorted(set(tpl13))[1])

# 14
element14 = 5
print((element14,))

# 15
lst15tpl = [1, 2, 3]
print(tuple(lst15tpl))

# 16
tpl16 = (1, 2, 3, 4, 5)
print(tpl16 == tuple(sorted(tpl16)))

# 17
tpl17 = (1, 2, 3, 4, 5)
print(max(tpl17[1:4]))

# 18
tpl18 = (1, 2, 3, 4, 5)
print(min(tpl18[1:4]))

# 19
tpl19 = (1, 2, 3, 2, 4)
lst19tpl = list(tpl19)
lst19tpl.remove(2)
print(tuple(lst19tpl))



# 22
tpl22 = tuple(range(1, 11))
print(tpl22)

# 23
tpl23 = (1, 2, 3, 4, 5)
print(tpl23[::-1])

# 24
tpl24 = (1, 2, 3, 2, 1)
print(tpl24 == tpl24[::-1])




# SET

# 1
set1a = {1, 2, 3}
set1b = {3, 4, 5}
print(set1a | set1b)

# 2
set2a = {1, 2, 3}
set2b = {2, 3, 4}
print(set2a & set2b)

# 3
set3a = {1, 2, 3}
set3b = {2, 3, 4}
print(set3a - set3b)

# 4
set4a = {1, 2}
set4b = {1, 2, 3, 4}
print(set4a.issubset(set4b))

# 5
set5 = {1, 2, 3, 4, 5}
print(3 in set5)

# 6
set6 = {1, 2, 3, 4, 5}
print(len(set6))

# 7
lst7set = [1, 2, 2, 3, 3, 4]
print(set(lst7set))

# 8
set8 = {1, 2, 3, 4, 5}
set8.discard(3)
print(set8)

# 9
set9 = set()
print(set9)

# 10
set10 = set()
print(len(set10) == 0)

# 11
set11a = {1, 2, 3}
set11b = {3, 4, 5}
print(set11a ^ set11b)

# 12
set12 = {1, 2, 3}
set12.add(4)
print(set12)

# 13
set13 = {1, 2, 3, 4, 5}
print(set13.pop())

# 14
set14 = {1, 2, 3, 4, 5}
print(max(set14))

# 15
set15 = {1, 2, 3, 4, 5}
print(min(set15))

# 16
set16 = {1, 2, 3, 4, 5, 6}
print({x for x in set16 if x % 2 == 0})

# 17
set17 = {1, 2, 3, 4, 5, 6}
print({x for x in set17 if x % 2 != 0})

# 18
set18 = set(range(1, 11))
print(set18)

# 19
lst19a = [1, 2, 3]
lst19b = [3, 4, 5]
print(set(lst19a + lst19b))

# 20
set20a = {1, 2, 3}
set20b = {4, 5, 6}
print(set20a.isdisjoint(set20b))

# 21
lst21 = [1, 2, 2, 3, 3, 4]
print(list(set(lst21)))

# 22
lst22 = [1, 2, 2, 3, 3, 4]
print(len(set(lst22)))

# 23
import random
set23 = {random.randint(1, 100) for _ in range(10)}
print(set23)


# DICTIONARY

# 1
dict1 = {'a': 1, 'b': 2, 'c': 3}
print(dict1.get('b'))

# 2
dict2 = {'a': 1, 'b': 2, 'c': 3}
print('b' in dict2)

# 3
dict3 = {'a': 1, 'b': 2, 'c': 3}
print(len(dict3))

# 4
dict4 = {'a': 1, 'b': 2, 'c': 3}
print(list(dict4.keys()))

# 5
dict5 = {'a': 1, 'b': 2, 'c': 3}
print(list(dict5.values()))

# 6
dict6a = {'a': 1, 'b': 2}
dict6b = {'c': 3, 'd': 4}
print({**dict6a, **dict6b})

# 7
dict7 = {'a': 1, 'b': 2, 'c': 3}
dict7.pop('b', None)
print(dict7)

# 8
dict8 = {}
print(dict8)

# 9
dict9 = {}
print(len(dict9) == 0)

# 10
dict10 = {'a': 1, 'b': 2, 'c': 3}
key10 = 'b'
print((key10, dict10[key10]) if key10 in dict10 else None)

# 11
dict11 = {'a': 1, 'b': 2, 'c': 3}
dict11['b'] = 99
print(dict11)

# 12
dict12 = {'a': 1, 'b': 2, 'c': 1, 'd': 3}
print(list(dict12.values()).count(1))

# 13
dict13 = {'a': 1, 'b': 2, 'c': 3}
print({v: k for k, v in dict13.items()})

# 14
dict14 = {'a': 1, 'b': 2, 'c': 1}
value14 = 1
print([k for k, v in dict14.items() if v == value14])

# 15
keys15 = ['a', 'b', 'c']
values15 = [1, 2, 3]
print(dict(zip(keys15, values15)))

# 16
dict16 = {'a': 1, 'b': {'c': 2}}
print(any(isinstance(v, dict) for v in dict16.values()))

# 17
dict17 = {'a': {'b': {'c': 3}}}
print(dict17['a']['b']['c'])



# 19
dict19 = {'a': 1, 'b': 2, 'c': 1, 'd': 3}
print(len(set(dict19.values())))

# 20
dict20 = {'c': 3, 'a': 1, 'b': 2}
print(dict(sorted(dict20.items())))

# 21
dict21 = {'a': 3, 'b': 1, 'c': 2}
print(dict(sorted(dict21.items(), key=lambda x: x[1])))

# 22
dict22 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print({k: v for k, v in dict22.items() if v > 2})

# 23
dict23a = {'a': 1, 'b': 2}
dict23b = {'b': 3, 'c': 4}
print(bool(set(dict23a.keys()) & set(dict23b.keys())))



# 25
dict25 = {'a': 1, 'b': 2, 'c': 3}
first25 = next(iter(dict25.items()))
print(first25)