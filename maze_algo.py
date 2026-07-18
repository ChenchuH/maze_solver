import random


def maze(size: int) -> list[list[str]]:
    """
    Generate a random perfect square maze.

    maze(10) creates:
    - 10 x 10 logical cells
    - 21 x 21 printed positions
    """

    if size < 1:
        raise ValueError("Maze size must be at least 1.")

    width = 2 * size + 1

    # Begin with everything being a wall.
    grid = [["[]" for _ in range(width)] for _ in range(width)]

    # Each logical cell becomes an empty space.
    for row in range(size):
        for column in range(size):
            grid[2 * row + 1][2 * column + 1] = "  "

    visited = [[False for _ in range(size)] for _ in range(size)]

    # Start in the upper-left logical cell.
    stack = [(0, 0)]
    visited[0][0] = True

    directions = [
        (-1, 0),  # up
        (1, 0),   # down
        (0, -1),  # left
        (0, 1),   # right
    ]

    while stack:
        row, column = stack[-1]

        available_neighbors = []

        for row_change, column_change in directions:
            new_row = row + row_change
            new_column = column + column_change

            inside_maze = (
                0 <= new_row < size
                and 0 <= new_column < size
            )

            if inside_maze and not visited[new_row][new_column]:
                available_neighbors.append(
                    (new_row, new_column, row_change, column_change)
                )

        if available_neighbors:
            new_row, new_column, row_change, column_change = (
                random.choice(available_neighbors)
            )

            # Remove the wall between the current cell and new cell.
            wall_row = 2 * row + 1 + row_change
            wall_column = 2 * column + 1 + column_change
            grid[wall_row][wall_column] = "  "

            visited[new_row][new_column] = True
            stack.append((new_row, new_column))
        else:
            # No available neighbor, so backtrack.
            stack.pop()

    # Entrance and exit.
    grid[1][0] = "  "
    grid[-2][-1] = "  "

    return grid


def print_maze(grid: list[list[str]]) -> None:
    for row in grid:
        print("".join(row))

def break_random_walls(grid, amount=5):
    rows = len(grid)
    columns = len(grid[0])

    candidates = []

    for row in range(1, rows - 1):
        for column in range(1, columns - 1):
            if grid[row][column] != "[]":
                continue

            # Horizontal wall between two open cells.
            if grid[row][column - 1] == "  " and grid[row][column + 1] == "  ":
                candidates.append((row, column))

            # Vertical wall between two open cells.
            elif grid[row - 1][column] == "  " and grid[row + 1][column] == "  ":
                candidates.append((row, column))

    random.shuffle(candidates)

    for row, column in candidates[:amount]:
        grid[row][column] = "  "


grid = maze(10)
break_random_walls(grid, amount=8)
print_maze(grid)