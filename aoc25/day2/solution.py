import re


def parse_input(lines: list[str]) -> list[range]:
    pairs = lines[0].split(",")
    ranges = list[range]()
    for pair in pairs:
        r = pair.split("-")
        ranges.append(range(int(r[0]), int(r[1]) + 1))

    return ranges


re_part1 = r"^(\d*)\1{1}$"
re_part2 = r"^(\d*)\1+$"


def is_invalid(num: int, part2: bool = False) -> bool:
    num_str = str(num)

    if part2:
        return re.match(re_part2, num_str) is not None

    return re.match(re_part1, num_str) is not None


def part1(ranges: list[range]) -> None:
    invalids = set(num for range in ranges for num in range if is_invalid(num))

    print(f"Part 1: {sum(invalids)}")


def part2(ranges: list[range]) -> None:
    invalids = set(num for range in ranges for num in range if is_invalid(num, True))

    print(f"Part 2: {sum(invalids)}")


def main(lines: list[str]) -> None:
    ranges = parse_input(lines)
    part1(ranges)
    part2(ranges)
