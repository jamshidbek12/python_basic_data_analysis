import numpy as np

# Task 1
vector_t1 = np.arange(10, 50)
print(vector_t1)

# Task 2
arr2 = np.array([
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ]
])
print(arr2)

# Task 3
arr3 = np.eye(3,3, dtype=int)
print(arr3)

# Task 4
arr4 = np.random.random((3,3,3))
print(arr4)

# Task 5
arr5 = np.random.random((10,10))
min_arr5 = arr5.min()
max_arr5 = arr5.max()
print(arr5)
print(min_arr5)
print(max_arr5)

# Task 6
arr6 = np.random.random(30)
print(arr6.mean())

# Task 7
arr7 = np.random.uniform(1, 100, (5, 5))
print("Original matritsa:")
print(arr7)

normalized_arr7 = (arr7 - arr7.min()) / (arr7.max() - arr7.min())
print("\nNormalized matritsa (0 dan 1 gacha):")
print(normalized_arr7)

# Task 8
arr8_1 = np.random.uniform(1, 100, (5, 3))
arr8_2 = np.random.uniform(1, 100, (3, 2))
res_arr8 = np.matmul(arr8_1, arr8_2)
print(res_arr8)

# Task 9
arr9_1 = np.random.uniform(1, 100, (3, 3))
arr9_2 = np.random.uniform(1, 100, (3, 3))
res_1_9 = arr9_1.astype(int)
res_2_9 = arr9_2.astype(int)
res_9 = np.dot(res_1_9, res_2_9)
print(res_1_9)
print(res_2_9)
print(res_9)

# 10
arr10 = np.random.uniform(1, 100, (4, 4))
res_10 = arr10.astype(int)
print(res_10.T)

# 11
arr11 = np.random.uniform(1, 100, (3, 3))
res_11 = np.linalg.det(arr11)
print(arr11)
print(res_11)

# 12
arr12_1 = np.random.uniform(1, 100, (3, 4))
arr12_2 = np.random.uniform(1, 100, (4, 3))
a_12 = arr12_1.astype(int)
b_12 = arr12_2.astype(int)
res_12 = np.dot(a_12, b_12)
print(a_12)
print(b_12)
print(res_12)

# 13
arr13 = np.random.uniform(1, 100, (3, 3))
vec13 = np.random.uniform(1, 100, (3, 1))
a_13 = arr13.astype(int)
b_13 = vec13.astype(int)
res13 = a_13 @ b_13
print(a_13)
print(b_13)
print(res13)

# 14
arr_14_1 = np.random.uniform(1, 100, (3, 3))
arr_14_2 = np.random.uniform(1, 100, (3, 1))
a_14 = arr_14_1.astype(int)
b_14 = arr_14_2.astype(int)
res14 = np.linalg.solve(a_14, b_14)
print(a_14)
print(b_14)
print(res14)

# 15
arr_15 = np.random.uniform(1, 100, (5, 5))
a_15 = arr_15.astype(int)

row_sum = np.sum(a_15, axis=1)
col_sum = np.sum(a_15, axis=0)
print(a_15)
print(row_sum)
print(col_sum)