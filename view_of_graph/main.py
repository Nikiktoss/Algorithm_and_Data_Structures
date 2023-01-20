if __name__ == '__main__':
    with open("input.txt") as file:
        size = int(file.readline())
        matrix_of_sides = []
        for line in file:
            matrix_of_sides.append([int(i) for i in line.strip().split()])

    result_array = [0] * size
    for row in matrix_of_sides:
        result_array[row[1] - 1] = row[0]

    with open("output.txt", "w") as file:
        print(*result_array, file=file)
