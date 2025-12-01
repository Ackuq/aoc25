def parse_input(lines: list[str]) -> list[int]:
    input = []
    for line in lines:
        if line.startswith("L"):
            input.append(-int(line.split("L")[1]))
            continue
        input.append(int(line.split("R")[1]))
    return input


def part1(rotations: list[int]) -> None:
    curr = 50
    solution = 0
    for rotation in rotations:
        curr = (curr + rotation) % 100
        if curr == 0:
            solution += 1

    print(f"Part 1: {solution}")


def part2(rotations: list[int]) -> None:
    curr = 50
    solution = 0
    for rotation in rotations:
        full_rotations = abs(rotation) // 100
        solution += full_rotations
        remainder = rotation - full_rotations * 100
        if remainder < 0 and curr != 0 and (curr + remainder) <= 0:
            solution += 1
        elif remainder > 0 and (curr + remainder) >= 100:
            solution += 1

        curr = (curr + rotation) % 100
    print(f"Part 2: {solution}")


"""
for (const move of input) {
  const rotations = Math.abs(Math.trunc(move / 100))
  const rest = move % 100

  const sum = pos + rest

  if (rest !== 0  && pos !== 0 && (sum <=0 || sum >=100)) {
    part2++
  }

  part2 += rotations
  pos = mod(pos + move, 100)

  if (pos === 0) {
    part1++
  }
}
"""


def main(lines: list[str]) -> None:
    input = parse_input(lines)
    part1(input)
    part2(input)
