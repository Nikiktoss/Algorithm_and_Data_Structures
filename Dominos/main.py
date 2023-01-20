def DFS(index, counter, matrix, bool_array):
    bool_array[index] = True
    counter += 1
    for elem in matrix[index]:
        if bool_array[elem] is False:
            counter, bool_array = DFS(elem, counter, matrix, bool_array)

    return counter, bool_array


if __name__ == '__main__':
    result = "Yes"
    with open("input.txt") as file:
        num_of_domino = int(file.readline().strip())
        matrix_of_domino = []

        for line in file:
            matrix_of_domino.append([int(i) for i in line.strip().split()])

    is_visited = [True] * 7
    matrix_of_relation = [[] for _ in range(7)]

    for i in range(num_of_domino):
        matrix_of_relation[matrix_of_domino[i][0]].append(matrix_of_domino[i][1])
        matrix_of_relation[matrix_of_domino[i][1]].append(matrix_of_domino[i][0])
        is_visited[matrix_of_domino[i][0]] = False
        is_visited[matrix_of_domino[i][1]] = False

    num_of_connected_vertex, num_of_not_visited_vertex = 0, 0
    for i in range(7):
        if is_visited[i] is False:
            num_of_not_visited_vertex += 1

    for i in range(7):
        if is_visited[i] is False:
            num_of_connected_vertex, is_visited = DFS(i, num_of_connected_vertex, matrix_of_relation, is_visited)
            break

    if num_of_connected_vertex != num_of_not_visited_vertex:
        result = "No"
    else:
        for i in range(7):
            if len(matrix_of_relation[i]) % 2 != 0:
                result = "No"
                break
    with open("output.txt", "w") as file:
        file.write(result)
