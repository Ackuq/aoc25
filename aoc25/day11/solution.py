from collections import deque


def parse_input(lines: list[str]) -> dict[str, set[str]]:
    return {
        parts[0]: {out for out in parts[1].split()}
        for line in lines
        if (parts := line.strip().split(": "))
    }


def part1(mapping: dict[str, set[str]]) -> None:
    paths = 0

    queue = deque([("you", frozenset(["you"]))])

    while queue:
        curr, seen = queue.popleft()

        if curr == "out":
            paths += 1
            continue

        for neighbor in mapping[curr]:
            if neighbor in seen:
                continue
            queue.append((neighbor, seen.union([neighbor])))

    print(f"Part 1: {paths}")


def part2(mapping: dict[str, set[str]]) -> None:
    def find_path(
        curr: str, target: str, ignore: set[str], memo: dict[str, int]
    ) -> int:
        if curr == target:
            return 1
        res = 0
        for neighbor in mapping[curr]:
            if neighbor in ignore:
                continue
            if neighbor in memo:
                res += memo[neighbor]
                continue
            res += find_path(neighbor, target, ignore, memo)
        memo[curr] = res
        return res

    svr_dac = find_path("svr", "dac", {"fft", "out"}, {})
    dac_fft = find_path("dac", "fft", {"svr", "out"}, {})
    fft_out = find_path("fft", "out", {"svr", "dac"}, {})

    svr_fft = find_path("svr", "fft", {"dac", "out"}, {})
    fft_dac = find_path("fft", "dac", {"svr", "out"}, {})
    dac_out = find_path("dac", "out", {"svr", "fft"}, {})

    paths = max(svr_fft * fft_dac * dac_out, svr_dac * dac_fft * fft_out)

    print(f"Part 2: {paths}")


def main(lines: list[str]) -> None:
    mapping = parse_input(lines)
    if "you" in mapping:
        part1(mapping)
    if "svr" in mapping:
        part2(mapping)
