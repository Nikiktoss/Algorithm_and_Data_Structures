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


if __name__ == '__main__':
    with open("input.txt") as file:
        city_require = [int(i) for i in file.readline().strip().split()]
        roads = []

        for line in file:
            roads.append(line.strip())

my_DSU = DisjointSetUnion(city_require[0])
number_of_components = [0 for _ in range(city_require[1])]
iteration = 0
for road in roads:
    cities_names = [int(i) for i in road.split()]
    my_DSU.union(cities_names[0], cities_names[1])
    number_of_components[iteration] = my_DSU.number_of_components
    iteration += 1


with open("output.txt", "w") as file:
    print(*number_of_components, sep='\n', file=file)
