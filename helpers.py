def transpose(grid: list[str]):
    return [''.join(x) for x in zip(*grid)]

