def parse_input(lines: list[str]) -> list[list[int]]:
    joltages = list[list[int]]()
    for line in lines:
        nums = (i for i in list(str(line)) if i.isnumeric())
        numbers = list(map(int, nums))
        joltages.append(numbers)

    return joltages


def part1(joltages: list[list[int]]) -> None:
    solution = 0
    for joltage in joltages:
        first_value = max(joltage[:-1])
        max_index = joltage.index(first_value)
        second_value = max(joltage[(max_index + 1) :])
        solution += first_value * 10 + second_value

    print(f"Part 1: {solution}")


def part2(joltages: list[list[int]]) -> None:
    solution = 0
    for joltage in joltages:
        start = 0
        values = list[int]()
        for i in range(12):
            slice = (
                joltage[start : -(12 - i - 1)] if (12 - i - 1) != 0 else joltage[start:]
            )
            next_value = max(slice)
            max_index = slice.index(next_value)
            start += max_index + 1
            values.append(next_value)

        solution += sum((value * 10 ** (12 - i - 1)) for i, value in enumerate(values))

    print(f"Part 2: {solution}")


def main(lines: list[str]) -> None:
    joltages = parse_input(lines)
    part1(joltages)
    part2(joltages)
