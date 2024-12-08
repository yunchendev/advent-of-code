import re

with open("2024/day/3/input.txt", "r") as file:
    lines = file.readlines()


def calculate_mul_sum(memory):
    mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"  # matches mul(x,y)

    is_enabled = True
    total_sum = 0

    i = 0
    while i < len(memory):
        if memory[i : i + 7] == "don't()":
            is_enabled = False
            i += 7
        elif memory[i : i + 4] == "do()":
            is_enabled = True
            i += 4
        else:
            match = re.match(mul_pattern, memory[i:])
            if match:
                if is_enabled:
                    x, y = map(int, match.groups())
                    total_sum += x * y
                i += match.end()

            else:
                i += 1

    return total_sum


sum = 0

input = ""

for line in lines:
    input += line

print(calculate_mul_sum(input))
