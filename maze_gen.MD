1. Input a size.

2. If size is even, add 1.
   Example: 10 becomes 11.
   This makes the maze dimensions odd.

3. Create a size × size grid filled completely with "#".
   Every cell starts as a wall.

4. Define a recursive function called carve(row, col).

5. Start carving at position (1, 1).

6. Inside carve(row, col):
   Mark the current cell as open:
   maze[row][col] = " "

7. Create a list of possible moves:
   up    = (-2, 0)
   down  = (2, 0)
   left  = (0, -2)
   right = (0, 2)

8. Shuffle those four directions randomly.

9. For each direction in that shuffled list:
   Calculate the target cell:
   new_row = row + dr
   new_col = col + dc

10. Check if the target cell is valid:
    - inside the maze border
    - not already visited
    - currently still "#"

11. If the target cell is valid:
    Find the wall between current cell and target cell:
    wall_row = row + dr // 2
    wall_col = col + dc // 2

12. Knock down that wall:
    maze[wall_row][wall_col] = " "

13. Move into the target cell by calling:
    carve(new_row, new_col)

14. That recursive call repeats the same process:
    - mark current cell open
    - shuffle directions
    - try valid moves
    - carve deeper

15. If a cell has no valid moves, that carve call ends.

16. When a carve call ends, Python returns to the previous cell.

17. The previous cell continues checking any remaining directions from its shuffled list.

18. This keeps happening until every possible cell has been visited/carved.

19. After carving is finished:
    Set maze[1][1] = "S"

20. Set maze[size - 2][size - 2] = "E"

21. Convert each row from a list into a string.

22. Return the finished maze.