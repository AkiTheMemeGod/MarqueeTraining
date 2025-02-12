import numpy as np
rows, cols = len(matrix), len(matrix[0])
row_zero = [False] * rows
col_zero = [False] * cols
print(matrix)
for i in range(rows):
    for j in range(cols):
        if matrix[i][j] == 0:
            row_zero[i] = True
            col_zero[j] = True

for i in range(rows):
    if row_zero[i]:
        for j in range(cols):
            matrix[i][j] = 0

for j in range(cols):
    if col_zero[j]:
        for i in range(rows):
            matrix[i][j] = 0



