matrix = [
    [12, 3, 7, 4],
    [1, 24, 8, 5],
    [4, 6, 9, 18],
    [1, 3, 17, 5]
]

print('Масив:')
for a in matrix:
    print(a)

num_rows = len(matrix)
num_columns = len(matrix[0])
column_sums = [0] * num_columns
for row in matrix:
    for i in range(num_columns):
        column_sums[i] += row[i]
print("Суми стовпців дорівнюють:", column_sums)

column_order = sorted(range(len(column_sums)), key=lambda x: column_sums[x])

sorted_matrix = [[0] * num_columns for _ in range(num_rows)]
for k in range(num_columns):
    col_index = column_order[k]
    for j in range(num_rows):
        sorted_matrix[j][k] = matrix[j][col_index]
print('Відсортований масив:')
for row in sorted_matrix:
    print(row)
