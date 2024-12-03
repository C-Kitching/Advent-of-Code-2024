import re

def sum_valid_multiplications(memory):
    # Define a regular expression to capture valid mul(X,Y) instructions
    pattern = r"mul\(\s*(\d+)\s*,\s*(\d+)\s*\)"

    # Find all matches in the memory string
    matches = re.findall(pattern, memory)

    # Initialize a variable to store the sum of results
    total_sum = 0

    # Process each match
    for match in matches:
        # Extract the numbers and convert them to integers
        x, y = map(int, match)
        # Multiply the numbers and add the result to the total sum
        total_sum += x * y

    return total_sum


with open("./day3/input.txt", "r") as file:
    memory = file.read()

res = sum_valid_multiplications(memory)

print(res)