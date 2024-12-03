import re

def sum_valid_multiplications(memory):

    # Define a regular expression to capture valid mul(X,Y) instructions
    pattern = r"mul\(\s*(\d+)\s*,\s*(\d+)\s*\)"

    # Define regular expressions to capture do() and don't() instructions
    enable_pattern = r"do\(\)"
    disable_pattern = r"don't\(\)"

    # Find all mul instructions and their positions
    matches = [(m.start(), m.groups()) for m in re.finditer(pattern, memory)]

    # Find all do() and don't() instructions and their positions
    enable_positions = [m.start() for m in re.finditer(enable_pattern, memory)]
    disable_positions = [m.start() for m in re.finditer(disable_pattern, memory)]

    # Sort enable and disable positions together with their types
    state_changes = [(pos, 'enable') for pos in enable_positions] + [(pos, 'disable') for pos in disable_positions]
    state_changes.sort()

    # Process the memory to determine the state at each mul instruction
    total_sum = 0
    enabled = True  # Initial state: enabled
    state_index = 0

    for pos, groups in matches:
        # Update the enabled/disabled state based on the most recent do() or don't()
        while state_index < len(state_changes) and state_changes[state_index][0] < pos:
            _, state = state_changes[state_index]
            enabled = (state == 'enable')
            state_index += 1

        # If enabled, process the mul instruction
        if enabled:
            x, y = map(int, groups)
            total_sum += x * y

    return total_sum

with open("./day3/input.txt", "r") as file:
    memory = file.read()

res = sum_valid_multiplications(memory)

print(res)