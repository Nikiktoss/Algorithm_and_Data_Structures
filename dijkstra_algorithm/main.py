import heapq


if __name__ == '__main__':
    with open("input.txt") as file:
        vertex_side = [int(i) for i in file.readline().strip().split()]
        matrix = [[] for _ in range(vertex_side[0])]

        for line in file:
            tmp = [int(i) for i in line.strip().split()]
            matrix[tmp[0] - 1].append((tmp[2], tmp[1]))
            matrix[tmp[1] - 1].append((tmp[2], tmp[0]))

    is_visited = [False] * vertex_side[0]
    distance = [10 ** 20] * vertex_side[0]

    distance[0] = 0
    pair = [(0, 0)]
    heapq.heapify(pair)

    while len(pair) != 0:
        pair_to_work = heapq.heappop(pair)

        if is_visited[pair_to_work[1]] is True:
            continue
        else:
            is_visited[pair_to_work[1]] = True
            distance[pair_to_work[1]] = pair_to_work[0]

            for elem in matrix[pair_to_work[1]]:
                print(elem)
                if is_visited[elem[1] - 1] is False and distance[pair_to_work[1]] + elem[0] < distance[elem[1] - 1]:
                    heapq.heappush(pair, (distance[pair_to_work[1]] + elem[0], elem[1] - 1))

    with open("output.txt", "w") as file:
        file.write(str(distance[-1]))
