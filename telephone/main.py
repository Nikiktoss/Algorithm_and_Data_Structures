def count_number_of_clicks(array_of_letters, buttons):
    if buttons == 1:
        result = 0
        for i in range(len(array_of_letters)):
            result += (array_of_letters[i] * (i + 1))
        return result
    elif buttons > len(array_of_letters):
        return sum(array_of_letters)
    else:
        matrix = [[0] * len(array_of_letters) for _ in range(buttons)]
        max_num_of_letters = len(array_of_letters) - buttons + 1
        for i in range(len(matrix)):
            num_of_clicks = 2
            for j in range(i, i + max_num_of_letters):
                if j == 0:
                    matrix[i][j] = array_of_letters[0]
                elif i == j:
                    matrix[i][j] = matrix[i - 1][j - 1] + array_of_letters[i]
                else:
                    matrix[i][j] = matrix[i][j - 1] + num_of_clicks * array_of_letters[j]
                    num_of_clicks += 1

            if i != 0:
                for j in range(i + 1,  i + max_num_of_letters):
                    num_of_clicks2 = 1
                    number = matrix[i - 1][j - 1]
                    for k in range(j, i + max_num_of_letters):
                        number += (num_of_clicks2 * array_of_letters[k])
                        num_of_clicks2 += 1

                        if number < matrix[i][k]:
                            matrix[i][k] = number

        return matrix[-1][-1]


with open("in.txt") as file:
    num_of_buttons = int(file.readline().strip())
    num_of_letters = int(file.readline().strip())
    value_letters = []

    for line in file:
        value_letters.append(int(line.strip()))

with open("out.txt", "w") as file:
    file.write(str(count_number_of_clicks(value_letters, num_of_buttons)))
