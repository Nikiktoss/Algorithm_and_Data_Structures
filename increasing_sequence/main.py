def upper_bound(array, number):
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


def count_max_len(array_of_elements):
    sequence = [array_of_elements[0]]
    indexes = [0]

    for i in range(1, len(array_of_elements)):
        indexes.append(upper_bound(sequence, array_of_elements[i]))

        if indexes[i] == len(sequence):
            sequence.append(array_of_elements[i])
        else:
            if array_of_elements[i] < sequence[indexes[i]]:
                sequence[indexes[i]] = array_of_elements[i]

    return len(sequence)


if __name__ == '__main__':
    with open("input.txt") as file:
        num_of_elements = int(file.readline().strip())
        elements = [int(i) for i in file.readline().strip().split()]

    with open("output.txt", "w") as file:
        file.write(str(count_max_len(elements)))
