if __name__ == '__main__':
    with open("input.txt") as file:
        size = [int(i) for i in file.readline().strip().split()]
        matrix_of_sides = []
        for line in file:
            matrix_of_sides.append([int(i) for i in line.strip().split()])

result_matrix = [[0] * size[0] for _ in range(size[0])]
for row in matrix_of_sides:
    result_matrix[row[0] - 1][row[1] - 1] = 1
    result_matrix[row[1] - 1][row[0] - 1] = 1

with open("output.txt", "w") as file:
    for res in result_matrix:
        print(*res, file=file)
