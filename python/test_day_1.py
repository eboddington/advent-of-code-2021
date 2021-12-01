from day_1 import num_times_increases, num_times_increases_sliding_window


EXAMPLE_INPUT = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]


def test_part_1_example_input():
    assert num_times_increases(EXAMPLE_INPUT) == 7


def test_part_2_example_input():
    assert num_times_increases_sliding_window(EXAMPLE_INPUT) == 5
