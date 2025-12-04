Coord = tuple[int, int]


def parse_input(lines: list[str]) -> set[Coord]:
    rolls = set[Coord](
        (x, y)
        for y, line in enumerate(lines)
        for x, char in enumerate(line.strip())
        if char == "@"
    )
    return rolls


def neighbor_count(roll: Coord, rolls: set[Coord]) -> int:
    count = sum(
        1
        for dx in range(-1, 2)
        for dy in range(-1, 2)
        if (dx != 0 or dy != 0) and (roll[0] + dx, roll[1] + dy) in rolls
    )

    return count


def part1(rolls: set[Coord]) -> None:
    solution = sum(1 for roll in rolls if neighbor_count(roll, rolls) < 4)

    print(f"Part 1: {solution}")


def part2(rolls: set[Coord]) -> None:
    solution = 0

    def to_remove():
        return {roll for roll in rolls if neighbor_count(roll, rolls) < 4}

    while removable := to_remove():
        solution += len(removable)
        rolls -= removable

    print(f"Part 2: {solution}")


def main(lines: list[str]) -> None:
    rolls = parse_input(lines)
    part1(rolls)
    part2(rolls)
