if __name__ == '__main__':
    with open("input.txt") as file:
        size = [int(i) for i in file.readline().strip().split()]
        matrix_of_sides = []
        for line in file:
            matrix_of_sides.append([int(i) for i in line.strip().split()])

    list_of_arrays = [[0] for i in range(size[0])]

    for row in matrix_of_sides:
        list_of_arrays[row[0] - 1][0] += 1
        list_of_arrays[row[0] - 1].append(row[1])

        list_of_arrays[row[1] - 1][0] += 1
        list_of_arrays[row[1] - 1].append(row[0])

    with open("output.txt", "w") as file:
        for arr in list_of_arrays:
            print(*arr, file=file)
