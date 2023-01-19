def binary_search_bigger_equal(array, number):
    first, last = 0, len(array)

    if number > array[-1]:
        return len(array)

    while last > first:
        mid = (first + last) // 2

        if array[mid] >= number:
            last = mid
        else:
            first = mid + 1

    return first


def binary_search_bigger(array, number):
    first, last = 0, len(array)

    if number > array[-1]:
        return len(array)

    while last > first:
        mid = (first + last) // 2

        if array[mid] > number:
            last = mid
        else:
            first = mid + 1

    return first


if __name__ == '__main__':
    n = int(input())
    elements = [int(num) for num in input().split()]
    k = int(input())
    requests = [int(num) for num in input().split()]

    for req in requests:
        data = [0, -1, -1]

        data[1] = binary_search_bigger_equal(elements, req)
        data[2] = binary_search_bigger(elements, req)

        if data[1] != len(elements) and req == elements[data[1]]:
            data[0] = 1

        print(*data)
