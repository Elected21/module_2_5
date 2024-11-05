def get_matrix(n, m, value):
    matrix = []
    list_in_list = []
    for j in range(n):
        list_in_list.append(matrix)
    for i in range(m):
        matrix.append(value)

    return list_in_list

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)

print(result1)
print(result2)
print(result3)
