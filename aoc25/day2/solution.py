def parse_input(lines: list[str]) -> list[range]:
    pairs = lines[0].split(",")
    ranges = list[range]()
    for pair in pairs:
        r = pair.split("-")
        ranges.append(range(int(r[0]), int(r[1]) + 1))

    return ranges


possible_splits = [2, 3, 5, 7]


def is_invalid(num: int, part2: bool = False) -> bool:
    num_str = str(num)

    if not part2:
        if len(num_str) % 2 != 0:
            return False
        left_part = num_str[: len(num_str) // 2]
        right_part = num_str[len(num_str) // 2 :]

        return left_part == right_part

    for split in possible_splits:
        if len(num_str) % split != 0:
            continue

        part_length = len(num_str) // split
        parts = [num_str[i * part_length : (i + 1) * part_length] for i in range(split)]

        if all(part == parts[0] for part in parts):
            return True

    return False


def part1(ranges: list[range]) -> None:
    invalids = set[int]()
    for range in ranges:
        for num in range:
            if is_invalid(num):
                invalids.add(num)

    print(f"Part 1: {sum(invalids)}")


def part2(ranges: list[range]) -> None:
    invalids = set[int]()
    for range in ranges:
        for num in range:
            if is_invalid(num, True):
                invalids.add(num)

    print(f"Part 2: {sum(invalids)}")


def main(lines: list[str]) -> None:
    ranges = parse_input(lines)
    part1(ranges)
    part2(ranges)
