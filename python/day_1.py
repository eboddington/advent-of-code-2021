def num_times_increases(depths: list[int]) -> int:
    count = 0

    for i, depth in enumerate(depths):
        if i != 0 and depth > depths[i - 1]:
            count += 1

    return count


def num_times_increases_sliding_window(depths: list[int]) -> int:
    sliding_window_sums: list[int] = []
    increase_count = 0

    for i, depth in enumerate(depths):
        try:
            window = depths[i - 1], depth, depths[i + 1]
        except IndexError:
            continue
        else:
            this_window_sum = sum(window)

            if sliding_window_sums and this_window_sum > sliding_window_sums[-1]:
                increase_count += 1

            sliding_window_sums.append(this_window_sum)

    return increase_count

