from math import prod

Coord = tuple[int, int, int]


def parse_input(lines: list[str]) -> list[Coord]:
    coords: list[Coord] = []
    for line in lines:
        x, y, z = map(int, line.split(","))
        coords.append((x, y, z))
    return coords


def straight_line_distance(a: Coord, b: Coord) -> float:
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2) ** 0.5


def get_distances(coords: list[Coord]) -> list[tuple[float, int, int]]:
    n = len(coords)

    distances: list[tuple[float, int, int]] = []
    for i in range(n):
        for j in range(i + 1, n):
            distances.append((straight_line_distance(coords[i], coords[j]), i, j))

    distances.sort()

    return distances


def part1(coords: list[Coord]) -> None:
    n = len(coords)
    distances = get_distances(coords)
    connections = 10 if n == 20 else 1000

    circuit_map = {i: frozenset([i]) for i in range(n)}

    for _, i, j in distances[:connections]:
        new_set = circuit_map[i].union(circuit_map[j])
        for junction in new_set:
            circuit_map[junction] = new_set

    circuits = list(set(circuit_map.values()))
    circuits = sorted(circuits, key=lambda circuit: len(circuit), reverse=True)

    solution = prod(len(circuit) for circuit in circuits[:3])

    print(f"Part 1: {solution}")


def part2(coords: list[Coord]) -> None:
    n = len(coords)
    distances = get_distances(coords)
    circuit_map = {i: frozenset([i]) for i in range(n)}

    z = 0
    while len(list(set(circuit_map.values()))) != 1:
        _, i, j = distances[z]
        new_set = circuit_map[i].union(circuit_map[j])
        for junction in new_set:
            circuit_map[junction] = new_set
        z += 1

    _, i, j = distances[z - 1]

    solution = coords[i][0] * coords[j][0]

    print(f"Part 2: {solution}")


def main(lines: list[str]) -> None:
    coords = parse_input(lines)
    part1(coords)
    part2(coords)
