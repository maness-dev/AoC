from typing import Literal


STARTING_DIGIT = 50
TARGET_DIGIT = 0
HIT_TARGET_COUNT = 0
CURRENT_POSITION = STARTING_DIGIT


def direction_process(direction: Literal["L", "R"], rotation_count: int):
    global CURRENT_POSITION, TARGET_DIGIT, HIT_TARGET_COUNT

    match direction:
        case "L":
            CURRENT_POSITION = (CURRENT_POSITION - rotation_count) % 100
            # (5-213)%100
            # Modulo Equation: a%b = a - (b * floor(a/b))
            # (-208) - (100 * floor(-208/100))
            # (-208) - (100 * floor(-2.08))
            # (-208) - (100 * -3)
            # (-208) - (-300) = 92
        case "R":
            CURRENT_POSITION = (CURRENT_POSITION + rotation_count) % 100
            # (5+213)%100
            # Modulo Equation: a%b = a - (b * floor(a/b))
            # (218) - (100 * floor(218/100))
            # (218) - (100 * 2)
            # (218) - (200) = 18
        case _:
            raise ValueError("Invalid operator")

    if CURRENT_POSITION == TARGET_DIGIT:
        HIT_TARGET_COUNT += 1

    return CURRENT_POSITION


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
