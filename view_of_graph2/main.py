if __name__ == '__main__':
    with open("input.txt") as file:
        size = int(file.readline())
        matrix_of_sides = []
        for line in file:
            matrix_of_sides.append([int(i) for i in line.strip().split()])

    array_result = [0] * size
    for i in range(size):
        for j in range(size):
            if matrix_of_sides[i][j] == 1:
                array_result[j] = i + 1

    with open("output.txt", "w") as file:
        print(*array_result, file=file)
