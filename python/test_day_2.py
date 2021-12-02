from day_2 import get_new_position, get_new_position_with_aim

EXAMPLE_INPUT = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]


def test_part_one_example_input():
    assert get_new_position(EXAMPLE_INPUT) == 150


def test_part_two_example_input():
    assert get_new_position_with_aim(EXAMPLE_INPUT) == 900
