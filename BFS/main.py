if __name__ == '__main__':
    with open("input.txt") as file:
        n = int(file.readline().strip())
        matrix = []

        for line in file:
            matrix.append([int(i) for i in line.strip().split()])

    array_of_vertex = [0] * n
    is_visited = [False] * n
    index = 1
    temp = []

    for i in range(n):
        if is_visited[i] is False:
            array_of_vertex[i] = index
            index += 1
            is_visited[i] = True
            temp.append(i)

            while len(temp) != 0:
                elem = temp.pop(0)
                for j in range(n):
                    if matrix[elem][j] == 1 and is_visited[j] is False:
                        is_visited[j] = True
                        temp.append(j)
                        array_of_vertex[j] = index
                        index += 1

    with open("output.txt", "w") as file:
        print(*array_of_vertex, file=file)
