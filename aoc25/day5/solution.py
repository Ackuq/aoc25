from functools import reduce


def parse_input(lines: list[str]) -> tuple[list[range], list[int]]:
    i_delimiter = lines.index("\n")

    ranges = [
        range(int(split[0]), int(split[1]) + 1)
        for line in lines[:i_delimiter]
        if (split := line.strip().split("-"))
    ]
    numbers = list[int](int(line.strip()) for line in lines[i_delimiter + 1 :])

    return ranges, numbers


def part1(ranges: list[range], numbers: list[int]) -> None:
    solution = sum(1 for num in numbers if any(num in r for r in ranges))

    print(f"Part 1: {solution}")


def reduce_sorted_ranges(acc: list[range], curr: range) -> list[range]:
    if len(acc) == 0:
        return [curr]

    prev_range = acc[-1]
    if curr.start <= prev_range.stop:
        acc[-1] = range(prev_range.start, max(prev_range.stop, curr.stop))
        return acc

    return acc + [curr]


def part2(ranges: list[range]) -> None:
    reduced_ranges = reduce(
        reduce_sorted_ranges, sorted(ranges, key=lambda r: r.start), list[range]()
    )
    solution = sum(len(r) for r in reduced_ranges)

    print(f"Part 2: {solution}")


def main(lines: list[str]) -> None:
    ranges, numbers = parse_input(lines)
    part1(ranges, numbers)
    part2(ranges)
