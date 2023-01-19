import heapq
from collections import deque


def greatest_common_divisor(a, b):
    if b == 0:
        return a
    else:
        return greatest_common_divisor(b, a % b)


def nok(a, b):
    return (a / greatest_common_divisor(a, b)) * b


if __name__ == '__main__':
    with open("input.txt") as file:
        num_of_rooms = int(file.readline().strip())
        num_of_gadgets = int(file.readline().strip())
        matrix = [[] for _ in range(num_of_rooms)]
        edges = []
        s = 0
        position = 1
        for line in file:
            tmp = [int(i) for i in line.strip().split()]
            matrix[tmp[0] - 1].append((nok(tmp[1], tmp[3]), tmp[2], position))
            matrix[tmp[2] - 1].append((nok(tmp[1], tmp[3]), tmp[0], position))
            edges.append((tmp[0], tmp[2]))
            position += 1

    is_visited = [False] * num_of_rooms
    distance = [10 ** 20] * num_of_rooms
    way = [-1] * num_of_rooms

    pair = [(0, 0, 0)]

    heapq.heapify(pair)
    while len(pair) != 0:
        pair_to_work = heapq.heappop(pair)

        if is_visited[pair_to_work[1]] is True:
            continue
        else:
            is_visited[pair_to_work[1]] = True
            distance[pair_to_work[1]] = pair_to_work[0]
            way[pair_to_work[1]] = pair_to_work[2]

            for elem in matrix[pair_to_work[1]]:
                if is_visited[elem[1] - 1] is False and distance[pair_to_work[1]] + elem[0] - \
                        distance[pair_to_work[1]] % elem[0] < distance[elem[1] - 1]:
                    heapq.heappush(pair, (distance[pair_to_work[1]] + elem[0] - distance[pair_to_work[1]] % elem[0],
                                          elem[1] - 1, elem[2]))

    index = num_of_rooms - 1
    result = deque()
    while index > 0:
        result.appendleft(way[index])
        if index + 1 != edges[way[index] - 1][0]:
            index = edges[way[index] - 1][0] - 1
        else:
            index = edges[way[index] - 1][1] - 1

    with open("output.txt", "w") as file:
        print(distance[-1] + 0.5, file=file)
        print(*result, file=file)
