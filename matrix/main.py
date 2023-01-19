def min_number_of_operations(array_of_matrix, size):
    matrix_result = [[0] * size for _ in range(size)]

    for diagonal in range(size - 1):
        for i in range(size - diagonal - 1):
            j = i + 1 + diagonal
            for k in range(i, j):
                temp_num = matrix_result[i][k] + matrix_result[k + 1][j] + \
                           array_of_matrix[i][0] * array_of_matrix[j][1]
                if matrix_result[i][j] == 0:
                    matrix_result[i][j] = temp_num
                else:
                    if temp_num < matrix_result[i][j]:
                        matrix_result[i][j] = temp_num

    return matrix_result[0][-1]


if __name__ == '__main__':
    num_of_cubes = int(input())
    matrix = []

    for _ in range(num_of_cubes):
        matrix.append([int(i) for i in input().split()])

    print(min_number_of_operations(matrix, num_of_cubes))
