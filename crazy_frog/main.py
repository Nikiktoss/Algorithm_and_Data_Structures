def count_mosquitoes(array_of_mosquitoes):

    values = [array_of_mosquitoes[0], -1] + ([0] * (len(array_of_mosquitoes) - 2))
    for i in range(len(array_of_mosquitoes) - 2):
        if i == 0:
            values[i] = array_of_mosquitoes[i]
        elif i == 1:
            values[i] = -1

        if values[i] == -1:
            continue
        else:
            if i + 2 <= len(array_of_mosquitoes) - 1:
                values[i + 2] = max(values[i + 2], array_of_mosquitoes[i + 2] + values[i])
            if i + 3 <= len(array_of_mosquitoes) - 1:
                values[i + 3] = max(values[i + 3], array_of_mosquitoes[i + 3] + values[i])

    if len(array_of_mosquitoes) == 1:
        print(array_of_mosquitoes[0])
        print(1)
    elif values[-1] == -1:
        print(values[-1])
    else:
        way = [len(array_of_mosquitoes)]
        counter = 1
        num = values[-1] - array_of_mosquitoes[way[0] - 1]
        while True:
            if way[-1] - 4 >= 0:
                way.append(values.index(num, way[-1] - 4, way[-1]) + 1)
            else:
                way.append(values.index(num) + 1)
            num -= array_of_mosquitoes[way[counter] - 1]
            counter += 1
            if way[-1] == 1:
                break

        print(values[-1])
        print(*way[::-1])


if __name__ == '__main__':
    n = int(input())
    bumps = list(map(int, input().split()))
    count_mosquitoes(bumps)
