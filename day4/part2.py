from pathlib import Path


def read_input_to_matrix(input: str) -> list:
    if Path(input).exists():
        with open(input) as f:
            input = f.read()

    output = []

    for line in input.strip().splitlines():
        output.append([c for c in line.strip()])

    return output


def part_two(input: str) -> int:
    mat = read_input_to_matrix(input)

    count_mats = 0

    for i in range(len(mat[0]) - 2):
        for j in range(len(mat) - 2):
            center = mat[j + 1][i + 1]
            top_left, bottom_right = mat[j][i], mat[j + 2][i + 2]
            top_right, bottom_left = mat[j][i + 2], mat[j + 2][i]

            cond_center = center == "A"
            cond_lr = (top_left == "M" and bottom_right == "S") or (
                top_left == "S" and bottom_right == "M"
            )
            cond_rl = (top_right == "M" and bottom_left == "S") or (
                top_right == "S" and bottom_left == "M"
            )

            if cond_center and cond_lr and cond_rl:
                count_mats += 1

    return count_mats

count = part_two("day4/input.txt")

print(count)