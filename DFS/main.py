def DFS(index, counter, matrix_sides, bool_array, array_result):
    bool_array[index] = True
    array_result[index] = counter
    counter += 1
    for i in range(len(matrix_sides[index])):
        if matrix_sides[index][i] == 1 and bool_array[i] is False:
            counter, bool_array, array_result = DFS(i, counter, matrix_sides, bool_array, array_result)

    return counter, bool_array, array_result


if __name__ == '__main__':
    with open("input.txt") as file:
        n = int(file.readline().strip())
        matrix = []

        for line in file:
            matrix.append([int(i) for i in line.strip().split()])

    is_visited = [False] * n
    result = [0] * n
    vertex_index = 1

    for i in range(n):
        if is_visited[i] is False:
            vertex_index, is_visited, result = DFS(i, vertex_index, matrix, is_visited, result)

    with open("output.txt", "w") as file:
        print(*result, file=file)
