class DisjointSetUnion:
    def __init__(self, n):
        self.parent = [i for i in range(1, n + 1)]
        self.size = [1 for _ in range(n)]
        self.number_of_components = n

    def find_parent(self, x):
        if x == self.parent[x - 1]:
            return x
        else:
            self.parent[x - 1] = self.find_parent(self.parent[x - 1])
            return self.parent[x - 1]

    def union(self, x, y):
        index_x = self.find_parent(x)
        index_y = self.find_parent(y)
        if index_x != index_y:
            if self.size[index_x - 1] < self.size[index_y - 1]:
                index_x, index_y = index_y, index_x

            self.size[index_x - 1] += self.size[index_y - 1]
            self.parent[index_y - 1] = index_x

            self.number_of_components -= 1

    def is_in_one_set(self, x, y):
        if self.find_parent(x) == self.find_parent(y):
            return True
        else:
            return False


if __name__ == '__main__':
    with open("equal-not-equal.in") as file:
        line = file.readline().strip().split()
        num_of_numbers = int(line[0])
        num_of_conditions = int(line[1])

        conditions = []
        for line in file:
            conditions.append(line.strip().split())

    my_dsu = DisjointSetUnion(num_of_numbers)
    for condition in conditions:
        if condition[1] == "==":
            my_dsu.union(int(condition[0][1:]), int(condition[2][1:]))

    result = ""

    for condition in conditions:
        if condition[1] == "!=":
            if my_dsu.is_in_one_set(int(condition[0][1:]), int(condition[2][1:])):
                result = "No"
                break
    else:
        result = "Yes"

    with open("equal-not-equal.out", "w") as file:
        file.write(result)
