from math import floor
from typing import Literal


STARTING_DIGIT = 50
TARGET_DIGIT = 0
HIT_TARGET_COUNT = 0
CURRENT_POSITION = STARTING_DIGIT


def direction_process(direction: Literal["L", "R"], rotation_count: int):
    global CURRENT_POSITION, TARGET_DIGIT, HIT_TARGET_COUNT

    # Count full laps
    HIT_TARGET_COUNT += floor(abs(rotation_count / 100))

    # Process the movement
    match direction:
        case "R":
            new_position = (CURRENT_POSITION + rotation_count) % 100
            # Count if we land on 0 OR if we wrap
            if new_position == TARGET_DIGIT or new_position < CURRENT_POSITION:
                HIT_TARGET_COUNT += 1
        case "L":
            new_position = (CURRENT_POSITION - rotation_count) % 100
            # Count if we land on 0 OR if we wrap (but not if we started at 0 or landed on 0)
            if new_position == TARGET_DIGIT or (
                new_position > CURRENT_POSITION
                and CURRENT_POSITION != TARGET_DIGIT
                and new_position != TARGET_DIGIT
            ):
                HIT_TARGET_COUNT += 1

    CURRENT_POSITION = new_position


def process_line(line: str):
    if line[0] not in ["L", "R"]:
        raise ValueError("Invalid direction")
    direction: Literal["L", "R"] = line[0]  # type: ignore[assignment]
    rotation_count = int(line[1:])
    direction_process(direction, rotation_count)


def main():
    with open("2025/Day1/directions.txt") as f:
        # with open("2025/Day1/sample_directions.txt") as f:
        for line in f:
            process_line(line.strip())
    print(HIT_TARGET_COUNT)


if __name__ == "__main__":
    main()
