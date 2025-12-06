def part1(lines: list[str]) -> None:
    numbers = [[num for num in line.strip().split()] for line in lines[:-1]]
    signs = lines[-1].strip().split()
    solution = sum(
        eval(f"{signs[i]}".join((row[i] for row in numbers))) for i in range(len(signs))
    )

    print(f"Part 1: {solution}")


def part2(lines: list[str]) -> None:
    solution = 0
    numbers: list[str] = []

    for col in range(len(lines[0]) - 1, -1, -1):
        current_number = ""
        operator: str | None = None

        for row in range(len(lines)):
            if col >= len(lines[row]):
                continue

            cell = lines[row][col]

            if cell.isnumeric():
                current_number += cell
            elif cell in ("*", "+"):
                operator = cell

        if current_number:
            numbers.append(current_number)

        if operator is not None:
            solution += eval(f"{operator}".join(numbers))
            numbers = []

    print(f"Part 2: {solution}")


def main(lines: list[str]) -> None:
    part1(lines)
    part2(lines)
