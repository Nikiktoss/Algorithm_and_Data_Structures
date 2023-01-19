def count_delta(symbol1, symbol2):
    if symbol1 == symbol2:
        return 0
    else:
        return 1


def count_number_of_operations(operations, string1, string2):
    matrix_of_operations = [[0] * (len(string2) + 1) for _ in range(len(string1) + 1)]

    for i in range(len(matrix_of_operations)):
        for j in range(len(matrix_of_operations[i])):
            if i == 0 and j != 0:
                matrix_of_operations[i][j] = j * operations[1]
            elif j == 0 and i != 0:
                matrix_of_operations[i][j] = i * operations[0]
            elif i == 0 and j == 0:
                matrix_of_operations[i][j] = 0
            else:
                count_delete = matrix_of_operations[i - 1][j] + operations[0]
                count_insert = matrix_of_operations[i][j - 1] + operations[1]
                count_replace = matrix_of_operations[i - 1][j - 1] + count_delta(string1[i - 1], string2[j - 1]) * min(
                    operations[2], operations[0] + operations[1])

                matrix_of_operations[i][j] = min(count_delete, count_insert, count_replace)

    for operation in matrix_of_operations:
        print(*operation)

    return matrix_of_operations[-1][-1]


with open("in.txt") as file:
    operation_cost = []
    for _ in range(3):
        operation_cost.append(int(file.readline().strip()))

    text1 = file.readline().strip()
    text2 = file.readline().strip()

with open("out.txt", "w") as file:
    file.write(str(count_number_of_operations(operation_cost, text1, text2)))
