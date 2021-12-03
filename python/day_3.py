from typing import TypeVar, Callable

T = TypeVar("T")


def get_power_consumption(binary_numbers: list[str]) -> int:
    """Part one"""
    nth_bits = _get_nth_bits(binary_numbers)

    gamma_rate = int("".join([_most_common_item(nth_bits[n]) for n in nth_bits]), 2)
    epsilon_rate = int("".join([_least_common_item(nth_bits[n]) for n in nth_bits]), 2)

    return gamma_rate * epsilon_rate


def get_life_support_rating(binary_numbers: list[str]) -> int:
    """Part two"""
    oxygen_generator_rating = _get_rating(
        binary_numbers=binary_numbers, bit_criteria=_most_common_item
    )
    co2_scrubber_rating = _get_rating(
        binary_numbers=binary_numbers, bit_criteria=_least_common_item
    )

    return oxygen_generator_rating * co2_scrubber_rating


def _get_rating(
    *, binary_numbers: list[str], bit_criteria: Callable[[list[T]], T], pos: int = 0
) -> int:
    nth_bits = _get_nth_bits(binary_numbers)

    filtered_by_bit_criteria = list(
        filter(lambda x: x[pos] == bit_criteria(nth_bits[pos]), binary_numbers)
    )

    if len(filtered_by_bit_criteria) == 1:
        return int(filtered_by_bit_criteria[0], 2)

    return _get_rating(
        binary_numbers=filtered_by_bit_criteria, bit_criteria=bit_criteria, pos=pos + 1
    )


def _get_nth_bits(binary_numbers: list) -> dict:
    """
    Basically rotates the data to look at columns, so turns:
    10110
    01001
    11100

    into:

    {
      0: [1, 0, 1],
      1: [0, 1, 1],
      2: [1, 0, 1]
      etc...
    }
    """
    return {
        n: [number[n] for number in binary_numbers]
        for n in range(len(binary_numbers[0]))
    }


def _most_common_item(items: list[T]) -> T:
    # we need to default to 1 if they are equally common
    num_ones = len([item for item in items if item == "1"])
    num_zeros = len([item for item in items if item == "0"])

    if num_ones == num_zeros or num_ones > num_zeros:
        return "1"

    return "0"


def _least_common_item(items: list[T]) -> T:
    return "1" if _most_common_item(items) == "0" else "0"
