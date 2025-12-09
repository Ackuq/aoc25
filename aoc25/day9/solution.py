from itertools import combinations

Coord = tuple[int, int]


def parse_input(lines: list[str]) -> list[Coord]:
    return [
        (int(coords[0]), int(coords[1]))
        for line in lines
        if (coords := line.split(","))
    ]


def get_area(a: Coord, b: Coord) -> int:
    return (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)


def part1(coords: list[Coord]) -> None:
    solution = get_area(
        max(coords, key=lambda coord: coord[0] + coord[1]),
        min(coords, key=lambda coord: coord[0] + coord[1]),
    )

    print(f"Part 1: {solution}")


def part2(coords: list[Coord]) -> None:
    def on_segment(coord: Coord, seg: tuple[Coord, Coord]):
        x, y = coord
        p, q = seg
        x1, y1 = p
        x2, y2 = q
        return x in range(min(x1, x2), max(x1, x2) + 1) and y in range(
            min(y1, y2), max(y1, y2) + 1
        )

    def is_point_in_bounds(coord: Coord) -> bool:
        # https://www.geeksforgeeks.org/dsa/how-to-check-if-a-given-point-lies-inside-a-polygon/
        inside = False
        x, y = coord
        for i in range(len(coords)):
            seg_start = coords[i]
            seg_end = coords[(i + 1) % len(coords)]
            if on_segment(coord, (seg_start, seg_end)):
                return True
            x1, y1 = seg_start
            x2, y2 = seg_end
            if y > min(y1, y2) and y <= max(y1, y2) and x <= max(x1, x2):
                x_intersection = (y - y1) * (x2 - x1) / (y2 - y1) + x1
                if x1 == x2 or x <= x_intersection:
                    inside = not inside
        return inside

    # -1 --> Clockwise
    # 0 --> p, q and r are collinear
    # 1 --> Counterclockwise
    def orientation(p: Coord, q: Coord, r: Coord) -> int:
        val = (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0])
        if val > 0:
            return 1
        if val < 0:
            return -1
        return 0

    def do_intersect(seg1: tuple[Coord, Coord], seg2: tuple[Coord, Coord]) -> bool:
        # https://www.geeksforgeeks.org/dsa/check-if-two-given-line-segments-intersect/

        o1 = orientation(seg1[0], seg1[1], seg2[0])
        o2 = orientation(seg1[0], seg1[1], seg2[1])
        o3 = orientation(seg2[0], seg2[1], seg1[0])
        o4 = orientation(seg2[0], seg2[1], seg1[1])

        return o1 * o2 < 0 and o3 * o4 < 0

    def is_valid_rect(a: Coord, b: Coord):
        x1, y1 = a
        x2, y2 = b
        for x, y in [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]:
            if not is_point_in_bounds((x, y)):
                return False
        for seg in [
            ((x1, y1), (x2, y1)),
            ((x2, y1), (x2, y2)),
            ((x2, y2), (x1, y2)),
            ((x1, y2), (x1, y1)),
        ]:
            for i in range(len(coords)):
                if do_intersect(seg, (coords[i], coords[(i + 1) % len(coords)])):
                    return False

        return True

    solution = 0
    for a, b in combinations(coords, 2):
        area = get_area(a, b)
        if area > solution and is_valid_rect(a, b):
            solution = area

    print(f"Part 2: {solution}")


def main(lines: list[str]) -> None:
    coords = parse_input(lines)
    part1(coords)
    part2(coords)
