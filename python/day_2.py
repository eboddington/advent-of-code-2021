from enum import Enum

class Direction(Enum):
    UP = "up"
    FORWARD = "forward"
    DOWN = "down"

class Command:
    def __init__(self, inp: str):
        direction, distance = tuple(inp.split(" "))
        self.direction = Direction(direction)
        self.distance = int(distance)


def get_new_position(course: list[str]) -> int:
    pos_horiz = 0
    pos_vert = 0

    for command in course:
        command = Command(command)

        match command.direction:
            case Direction.UP:
                pos_vert -= command.distance
            case Direction.DOWN:
                pos_vert += command.distance
            case Direction.FORWARD:
                pos_horiz += command.distance

    return pos_horiz * pos_vert
