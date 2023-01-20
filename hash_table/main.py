class HashTable:
    def __init__(self, m):
        self.hash_table = [-1 for _ in range(m)]

    def __hash_function(self, number, constanta, i):
        return ((number % len(self.hash_table)) + constanta * i) % len(self.hash_table)

    def add_element(self, x, c):
        index = 0
        while index != len(self.hash_table):
            if x == self.hash_table[self.__hash_function(x, c, index)]:
                break

            if self.hash_table[self.__hash_function(x, c, index)] == -1:
                self.hash_table[self.__hash_function(x, c, index)] = x
                break
            index += 1


if __name__ == '__main__':
    with open("input.txt") as file:
        mcn = [int(i) for i in file.readline().strip().split()]
        numbers = []
        for line in file:
            numbers.append(int(line))

    my_hash_table = HashTable(mcn[0])
    for i in range(len(numbers)):
        my_hash_table.add_element(numbers[i], mcn[1])

    with open("output.txt", "w") as file:
        print(*my_hash_table.hash_table, file=file)
