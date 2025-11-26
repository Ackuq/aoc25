# Advent of Code 2025

This repository contains my solutions for [Advent of Code 2025](https://adventofcode.com/2025).

## Development

### Prerequisites

```sh
uv python install
uv sync
```

### Formatting

```sh
uv run ruff check --select I --fix
uv run ruff format
```

### Linting

```sh
uv run ruff check --fix
```

## Running

The following script can be used for running the solution for each day:

```sh
uv run python -m aoc25 --day DAY [--example EXAMPLE] [--strip]
```

For example, if we want to run the solution for day 12, the command would be:

```sh
uv run python -m aoc25 --day 12
```
