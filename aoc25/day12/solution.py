Shape = list[tuple[int, int]]
Region = tuple[tuple[int, int], list[int]]

Input = tuple[list[Shape], list[Region]]


def parse_input(lines: list[str]) -> Input:
    shapes: list[Shape] = []
    regions: list[Region] = []

    i = 1
    while len(shapes) != 6:
        shape = [
            (x, y)
            for y, line in enumerate(lines[i : i + 4])
            for x, val in enumerate(line.strip())
            if val == "#"
        ]
        i += 5
        shapes.append(shape)

    i -= 1

    for line in lines[i:]:
        parts = line.strip().split(": ")
        dimensions = parts[0].split("x")
        dimensions = (int(dimensions[0]), int(dimensions[1]))
        quantities = [int(q) for q in parts[1].split()]
        regions.append((dimensions, quantities))

    return shapes, regions


def part1(shapes: list[Shape], regions: list[Region]) -> None:
    solution = 0
    for region in regions:
        area_region = region[0][0] * region[0][1]
        area_shapes = sum(len(shapes[i]) * x for i, x in enumerate(region[1]))
        if area_shapes > area_region:
            continue
        solution += 1

    print(f"Part 1: {solution}")


def part2(shapes: list[Shape], regions: list[Region]) -> None:
    pass


def main(lines: list[str]) -> None:
    shapes, regions = parse_input(lines)
    part1(shapes, regions)
    part2(shapes, regions)
