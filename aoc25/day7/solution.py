from collections import defaultdict


def part1(lines: list[str]) -> None:
    buffer = set()
    solution = 0

    for _, row in enumerate(lines):
        for x, char in enumerate(row):
            if char == "S":
                buffer.add(x)
                continue
            if char == "^" and x in buffer:
                solution += 1
                buffer.add(x + 1)
                buffer.add(x - 1)
                buffer.remove(x)

    print(f"Part 1: {solution}")


def part2(lines: list[str]) -> None:
    buffer: dict[int, int] = defaultdict(lambda: 0)

    for _, row in enumerate(lines):
        for x, char in enumerate(row):
            if char == "S":
                buffer[x] = 1
                continue
            if char == "^" and buffer[x] > 0:
                buffer[x - 1] += buffer[x]
                buffer[x + 1] += buffer[x]
                buffer[x] = 0

    solution = sum(buffer.values())

    print(f"Part 2: {solution}")


def main(lines: list[str]) -> None:
    part1(lines)
    part2(lines)
