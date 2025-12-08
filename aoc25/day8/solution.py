Coord = tuple[int, int, int]


def parse_input(lines: list[str]) -> list[Coord]:
    coords: list[Coord] = []
    for line in lines:
        x, y, z = map(int, line.split(","))
        coords.append((x, y, z))
    return coords


def straight_line_distance(a: Coord, b: Coord) -> float:
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2) ** 0.5


class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False

        if self.size[root_x] < self.size[root_y]:
            root_x, root_y = root_y, root_x

        self.parent[root_y] = root_x
        self.size[root_x] += self.size[root_y]
        return True

    def get_circuit_sizes(self) -> list[int]:
        circuits: dict[int, int] = {}
        for i in range(len(self.parent)):
            root = self.find(i)
            circuits[root] = self.size[root]
        return list(circuits.values())

    def num_circuits(self) -> int:
        roots = set()
        for i in range(len(self.parent)):
            roots.add(self.find(i))
        return len(roots)


def part1(coords: list[Coord]) -> None:
    n = len(coords)

    distances: list[tuple[float, int, int]] = []
    for i in range(n):
        for j in range(i + 1, n):
            dist = straight_line_distance(coords[i], coords[j])
            distances.append((dist, i, j))

    distances.sort()

    connections = 10 if n == 20 else 1000
    uf = UnionFind(n)

    for idx, (dist, i, j) in enumerate(distances):
        if idx >= connections:
            break
        uf.union(i, j)

    circuit_sizes = sorted(uf.get_circuit_sizes(), reverse=True)
    result = circuit_sizes[0] * circuit_sizes[1] * circuit_sizes[2]

    print(f"Part 1: {result}")


def part2(coords: list[Coord]) -> None:
    n = len(coords)

    distances: list[tuple[float, int, int]] = []
    for i in range(n):
        for j in range(i + 1, n):
            dist = straight_line_distance(coords[i], coords[j])
            distances.append((dist, i, j))

    distances.sort()

    uf = UnionFind(n)

    last_i, last_j = 0, 0
    for dist, i, j in distances:
        uf.union(i, j)
        if uf.num_circuits() == 1:
            last_i, last_j = i, j
            break

    result = coords[last_i][0] * coords[last_j][0]
    print(f"Part 2: {result}")


def main(lines: list[str]) -> None:
    coords = parse_input(lines)
    part1(coords)
    part2(coords)
