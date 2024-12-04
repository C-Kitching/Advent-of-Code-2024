
grid = []

with open("./day4/input.txt", "r") as file:
    for line in file:
        grid.append(list(line.strip()))

directions = [
    (0, 1),   # Right
    (1, 0),   # Down
    (1, 1),   # Down-right
    (1, -1),  # Down-left
    (0, -1),  # Left
    (-1, 0),  # Up
    (-1, -1), # Up-left
    (-1, 1)   # Up-right
]

rows = len(grid)
cols = len(grid[0])

target = "XMAS"

count = 0

def check_direction(x, y, dx, dy):
    for k in range(len(target)):
        nx = x+k*dx
        ny = y+k*dy
        if nx < 0 or nx >= rows or ny < 0 or ny >= cols or grid[nx][ny] != target[k]:
            return False
    return True

for i in range(rows):
    for j in range(cols):
        for dx, dy in directions:
            if check_direction(i, j, dx, dy):
                count += 1

print(count)