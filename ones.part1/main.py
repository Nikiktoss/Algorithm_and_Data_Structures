def pascal_triangle(list_n_k):
    result_row = [1, 1]

    for i in range(2, list_n_k[0] + 1):
        data = list(range(i + 1))

        data[0], data[-1] = 1, 1
        for j in range(1, len(result_row)):
            data[j] = result_row[j] + result_row[j - 1]
        result_row = data

    return result_row[list_n_k[1]]


if __name__ == '__main__':
    pair_n_k = [int(num) for num in input().split()]
    module = 10 ** 9 + 7

    print(pascal_triangle(pair_n_k) % module)
