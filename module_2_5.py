def get_matrix(m, n, value):
    matrix = []

    for i in range(n):
        matrix.append([])
        for k in range(m):
            matrix[i].append(value)
        i += 1
    return matrix


result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)
