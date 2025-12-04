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
    count = 0
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if dx == 0 and dy == 0:
                continue
            coord = (roll[0] + dx, roll[1] + dy)
            if coord in rolls:
                count += 1

    return count


def part1(rolls: set[Coord]) -> None:
    solution = 0
    for roll in rolls:
        if neighbor_count(roll, rolls) < 4:
            solution += 1

    print(f"Part 1: {solution}")


def part2(rolls: set[Coord]) -> None:
    solution = 0
    while True:
        has_changed = False
        new_rolls = rolls.copy()
        for roll in rolls:
            if neighbor_count(roll, rolls) < 4:
                solution += 1
                new_rolls.remove(roll)
                has_changed = True
        if not has_changed:
            break
        rolls = new_rolls

    print(f"Part 2: {solution}")


def main(lines: list[str]) -> None:
    rolls = parse_input(lines)
    part1(rolls)
    part2(rolls)
