from typing import TypeVar, Callable

T = TypeVar("T")


def most_common_item(items: list[T]) -> T:
    # we need to default to 1 if they are equally common
    ones = [item for item in items if item == "1"]
    zeros = [item for item in items if item == "0"]
    if len(ones) == len(zeros):
        return "1"
    return "1" if len(ones) > len(zeros) else "0"


def least_common_item(items: list[T]) -> T:
    return "1" if most_common_item(items) == "0" else "0"


def get_power_consumption(binary_numbers: list[str]) -> int:
    nth_bits = {
        n: [number[n - 1] for number in binary_numbers]
        for n in range(1, len(binary_numbers[0]) + 1)
    }
    gamma_rate = int("".join([most_common_item(nth_bits[n]) for n in nth_bits]), 2)

    epsilon_rate = int("".join([least_common_item(nth_bits[n]) for n in nth_bits]), 2)

    return gamma_rate * epsilon_rate


def get_life_support_rating(binary_numbers: list[str]) -> int:
    oxygen_generator_rating = _get_rating(binary_numbers, most_common_item)
    co2_scrubber_rating = _get_rating(binary_numbers, least_common_item)

    return oxygen_generator_rating * co2_scrubber_rating


def _get_rating(numbers: list, bit_criteria: Callable, pos: int = 0) -> int:
    nth_bits = _get_nth_bits(numbers)

    filtered_by_bit_criteria = list(
        filter(lambda x: x[pos] == bit_criteria(nth_bits[pos + 1]), numbers)
    )

    if len(filtered_by_bit_criteria) == 1:
        return int(filtered_by_bit_criteria[0], 2)

    return _get_rating(filtered_by_bit_criteria, bit_criteria, pos + 1)


def _get_nth_bits(numbers: list) -> dict:
    return {
        n: [number[n - 1] for number in numbers] for n in range(1, len(numbers[0]) + 1)
    }
