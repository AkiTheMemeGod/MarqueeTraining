import numpy as np
matrix = [[1,2,3,4], [4, 0, 6,7], [7,8,9,9]]
rows, cols = len(matrix), len(matrix[0])
row_zero = [0] * rows
col_zero = [0] * cols
print(matrix)
for i in range(rows):
    for j in range(cols):
        if matrix[i][j] == 0:
            row_zero[i] = 1
            col_zero[j] = 1

for i in range(rows):
    if row_zero[i]:
        for j in range(cols):
            matrix[i][j] = 0

for j in range(cols):
    if col_zero[j]:
        for i in range(rows):
            matrix[i][j] = 0

print(row_zero)
print(col_zero)

print(np.array(matrix))