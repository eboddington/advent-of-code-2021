from typing import Type, TypeVar

import day_1
import day_2

T = TypeVar("T")


def get_typed_lines_from_file(file_path: str, line_object_type: Type[T]) -> list[T]:
    with open(file_path, "r") as f:
        return [
            line_object_type(line) for line in filter(lambda l: l, f.read().split("\n"))
        ]


if __name__ == "__main__":
    day_1_part_1_result = day_1.num_times_increases(
        get_typed_lines_from_file("../inputs/day_1", int)
    )
    print(f"Day 1 part one: {day_1_part_1_result}")
    day_1_part_2_result = day_1.num_times_increases_sliding_window(
        get_typed_lines_from_file("../inputs/day_1", int)
    )
    print(f"Day 1 part two: {day_1_part_2_result}")

    day_2_part_one_result = day_2.get_new_position(get_typed_lines_from_file("../inputs/day_2", str))
    print(f"Day 2 part one: {day_2_part_one_result}")
