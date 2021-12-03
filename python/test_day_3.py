from day_3 import get_power_consumption, get_life_support_rating

EXAMPLE_INPUT = [
    "00100",
    "11110",
    "10110",
    "10111",
    "10101",
    "01111",
    "00111",
    "11100",
    "10000",
    "11001",
    "00010",
    "01010",
]


def test_get_power_consumption_example_input():
    assert get_power_consumption(EXAMPLE_INPUT) == 198


def test_get_life_support_rating():
    assert get_life_support_rating(EXAMPLE_INPUT) == 230
