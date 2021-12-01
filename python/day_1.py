def num_times_increases(depths: list[int]) -> int:
    count = 0

    for i, depth in enumerate(depths):
        if i != 0 and depth > depths[i - 1]:
            count += 1

    return count
