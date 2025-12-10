from collections import deque
from copy import deepcopy
from typing import cast

import pulp

Input = tuple[list[bool], list[set[int]], list[int]]


def parse_input(lines: list[str]) -> list[Input]:
    inputs: list[Input] = []

    for line in lines:
        parts = line.strip().split()
        diagram = [
            True if light == "#" else False
            for light in parts[0].removeprefix("[").removesuffix("]")
        ]
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
        queue = deque(([False] * len(diagram), button, 1) for button in buttons)
        seen: set[str] = set()
        while queue:
            curr, button, presses = queue.popleft()
            key = ",".join(str(b) for b in curr) + " " + str(button)
            if key in seen:
                continue
            seen.add(key)
            next_lights = deepcopy(curr)
            for num in button:
                next_lights[num] = not next_lights[num]

            if next_lights == diagram:
                solution += presses
                break

            queue.extend((next_lights, button, presses + 1) for button in buttons)

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

    print(f"Part 2: {min_sum}")


def main(lines: list[str]) -> None:
    input = parse_input(lines)
    part1(input)
    part2(input)
