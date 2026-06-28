import random

def generate_maze(size):
    if size % 2 == 0:
        size += 1

    width = size
    height = size 

    maze = [["#" for x in range(width)] for y in range(height)]

    def carve_path(row, col):
        maze[row][col] = " "

        directions = [(0, 2), (2, 0), (0, -2), (-2, 0)]

        random.shuffle(directions)

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 1 <= new_row < height - 1 and 1 <= new_col < width - 1:
                if maze[new_row][new_col] == "#":
                    maze[row + dr // 2][col + dc // 2] = " "
                    carve_path(new_row, new_col)
    
    carve_path(1, 1)
    maze[1][1] = "S"
    maze[size - 2][size - 2] = "E"
    return ["".join(row) for row in maze]

symbols = {
    "#": "[]",
    " ": "  ",
    "S": "X ",
    "E": "X ",
}

temp = generate_maze(10)
for row in temp:
    print("".join(symbols[c] for c in row))



