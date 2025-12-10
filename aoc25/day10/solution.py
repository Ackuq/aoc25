from collections import deque
from typing import cast

import pulp

Input = tuple[int, list[set[int]], list[int]]


def parse_input(lines: list[str]) -> list[Input]:
    inputs: list[Input] = []

    for line in lines:
        parts = line.strip().split()
        diagram = sum(
            1 << i
            for i, light in enumerate(parts[0].removeprefix("[").removesuffix("]"))
            if light == "#"
        )
        buttons = [
            {int(num) for num in button.removeprefix("(").removesuffix(")").split(",")}
            for button in parts[1:-1]
        ]
        joltages = [
            int(num) for num in parts[-1].removeprefix("{").removesuffix("}").split(",")
        ]
        inputs.append((diagram, buttons, joltages))

    return inputs


def part1(inputs: list[Input]) -> None:
    solution = 0
    for diagram, buttons, _ in inputs:
        n_buttons = len(buttons)
        queue = deque((0, i, 1) for i in range(n_buttons))
        seen: set[tuple[int, int]] = set()
        while queue:
            curr, i_button, presses = queue.popleft()
            if (curr, i_button) in seen:
                continue
            seen.add((curr, i_button))

            curr ^= sum(1 << num for num in buttons[i_button])

            if curr == diagram:
                solution += presses
                break

            queue.extend((curr, i, presses + 1) for i in range(n_buttons))

    print(f"Part 1: {solution}")


def part2(inputs: list[Input]) -> None:
    min_sum = 0
    for _, buttons, joltage_diagram in inputs:
        vars = [
            pulp.LpVariable(f"x{i}", cat=pulp.const.LpInteger, lowBound=0)
            for i in range(len(buttons))
        ]
        prob = pulp.LpProblem(sense=pulp.LpMinimize)
        prob += pulp.lpSum(vars)

        for i in range(len(joltage_diagram)):
            prob += (
                pulp.lpSum(vars[j] for j, button in enumerate(buttons) if i in button)
                == joltage_diagram[i]
            )

        prob.solve(pulp.PULP_CBC_CMD(msg=False))
        min_sum += cast(int, pulp.value(prob.objective))

    print(f"Part 2: {int(min_sum)}")


def main(lines: list[str]) -> None:
    input = parse_input(lines)
    part1(input)
    part2(input)
