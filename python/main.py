from typing import Type, TypeVar

import day_1

T = TypeVar("T")


def get_typed_lines_from_file(file_path: str, line_object_type: Type[T]) -> list[T]:
    with open(file_path, "r") as f:
        return [
            line_object_type(line) for line in filter(lambda l: l, f.read().split("\n"))
        ]


if __name__ == "__main__":
    day_1_result = day_1.num_times_increases(
        get_typed_lines_from_file("../inputs/day_1", int)
    )
    print(f"Day 1 result: {day_1_result}")
