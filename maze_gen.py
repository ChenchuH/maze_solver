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

    def add_loops(maze, count):
        height = len(maze)
        width = len(maze[0])

        for _ in range(count):
            row = random.randrange(2, height - 2, 2)
            col = random.randrange(2, width - 2, 2)

            if random.choice([True, False]):
                maze[row][col - 1] = " "
            else:
                maze[row - 1][col] = " "
    
    carve_path(1, 1)
    add_loops(maze, size // 2)
    
    maze[1][0] = " "
    maze[1][1] = "S"
    maze[size - 2][size - 2] = "E"
    maze[size - 2][size - 1] = " "
    return ["".join(row) for row in maze]
    #The E and S are the start and end points of the maze for internal logic, rendered as blank spaces for the output

GREEN = "\033[32m"
RESET = "\033[0m"
 
symbols = {
    "#": f"{GREEN}[]{RESET}",
    " ": "  ",
    "S": "  ",
    "E": "  ",
}

temp = generate_maze(20)
for row in temp:
    print("".join(symbols[c] for c in row))



