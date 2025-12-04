grid: list[list[str]] = []
ans = 0
with open("day 4/input.txt", "r") as f:
    for i, line in enumerate(f):
        grid.append(list())
        for char in line.strip():
            grid[i].append(char)

# direction offsets for each adjacent location
directions: list[tuple[int, int]] = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
]


def count_adjacent(matrix: list[list[str]], row: int, col: int):
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    adj: int = 0

    # check for each direction
    for dr, dc in directions:
        new_row = row + dr
        new_col = col + dc
        # check if in bounds
        if 0 <= new_row < rows and 0 <= new_col < cols:
            if matrix[new_row][new_col] != ".":
                adj += 1
    return adj


made_progress = True
while made_progress:
    prev_ans = ans
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            # skip empty cells
            if grid[row][col] == ".":
                continue

            if count_adjacent(grid, row, col) < 4:
                # if roll can be removed, we can mark it as removed
                grid[row][col] = "."
                ans += 1
    # stop loop as soon as we make no more progress
    made_progress = prev_ans != ans

print(ans)
