import random

WEST = 0
SOUTH = 1
EAST = 2
NORTH = 3


class MazeGenerator:
    """Generate and solve mazes.

    Attributes:
        width: Maze's number of columns.
        height: Maze's number of rows.
        entry: Start point (x, y) in the Maze.
        exit: Final point (x, y) in the Maze.
        output_file: Output file name.
        perfect: Generate a perfect Maze(only one path from entry to exit) if
                 True, and a Maze with multiple paths if False.
        seed: Optional seed to control randomness by producing the exact same
              Maze every time."""

    def __init__(self, width: int, height: int, entry: tuple[int, int],
                 exit: tuple[int, int], output_file: str, perfect: bool,
                 seed: int | None = None) -> None:
        self.width = width
        self.height = height
        self.entry = entry
        self.exit = exit
        self.output_file = output_file
        self.perfect = perfect
        self.seed = seed
        self.maze: list[list[list[int]]] = self.closed_grid_gen()
        self.pattern_42: list[tuple] = [(0, 0), (1, 0), (2, 0), (2, 1), (1, 2),
                                        (2, 2), (3, 2), (4, 2), (0, 4), (0, 5),
                                        (0, 6), (1, 6), (2, 4), (2, 5), (2, 6),
                                        (3, 4), (4, 4), (4, 5), (4, 6)]

    def closed_grid_gen(self) -> list:
        """Generate an initial grid with all four walls closed for each cell.
        Returns:
            A 3D list where each cell is [West, South, East, North] = [1,1,1,1]
        """
        grid: list = []
        r = 0
        for rows in range(self.height):
            grid.append([])
            c = 0
            for columns in range(self.width):
                closed_walls = [1, 1, 1, 1]
                grid[r] = grid[r] + [closed_walls]
                c += 1
            r += 1
        return grid

    def generate_maze_perfect(self) -> list[list[list[int]]]:
        """Generate a maze with only one path from entry point to
           exit point(perfect maze).

            Returns:
                A matrix list where every row is a list of cells and every cell
                is represented by 4 integers [West, South, East, North]
                (1=closed, 0=open)."""

        self.maze = self.closed_grid_gen()
        if self.seed is not None:
            random.seed(self.seed)
        path_stack: list = [self.entry]
        visited_list: list = [self.entry]
        self.close_42(visited_list)
        while path_stack:
            current_cell = path_stack[-1]
            all_neighbours_list = self.get_neighbours(current_cell)
            unvisited_neighbours = self.is_visited(all_neighbours_list,
                                                   visited_list)
            if unvisited_neighbours:
                next_cell = random.choice(unvisited_neighbours)
                self.open_wall(current_cell, next_cell)
                path_stack.append(next_cell)
                visited_list.append(next_cell)
            else:
                path_stack.pop()
        if not self.perfect:
            self.add_loops_maze()
        return self.maze
        # return mockup_maze

    def close_42(self, visited: list) -> None:
        """Mark the "42" pattern in the center as "visited" to keep its four
        walls closed"""

        if self.height >= 7 and self.width >= 9:
            row_first_42_cell = int((self.height - 5)/2)
            column_first_42_cell = int((self.width - 7)/2)
            i = 0
            for r, c in self.pattern_42:
                self.pattern_42[i] = (r + row_first_42_cell,
                                      c + column_first_42_cell)
                i += 1
            visited.extend(self.pattern_42)
        else:
            self.pattern_42 = []
            print("Error: Maze too small!")

    def get_neighbours(self,
                       current: tuple[int, int]) -> list[tuple[int, int]]:
        """Return a list of valid visited neighour cells"""
        row, column = current
        north: tuple = (row - 1, column)
        south: tuple = (row + 1, column)
        west: tuple = (row, column - 1)
        east: tuple = (row, column + 1)
        possible_neighbours: list[tuple[int, int]] = [north, south, west, east]
        valid_neighbours: list[tuple[int, int]] = []

        for neighbour in possible_neighbours:
            r, c = neighbour
            if 0 <= r < self.height and 0 <= c < self.width:
                valid_neighbours.append(neighbour)
        return valid_neighbours

    def is_visited(self, neighbours: list[tuple[int, int]],
                   visited: list[tuple[int, int]]) -> list[tuple[int, int]]:
        unvisited_neighbours: list[tuple[int, int]] = []
        for neighbour in neighbours:
            if neighbour not in visited:
                unvisited_neighbours.append(neighbour)
        return unvisited_neighbours

    def open_wall(self, current_cell: tuple[int, int],
                  next_cell: tuple[int, int]) -> None:
        """Open the shared wall betwenn current_cell and next_cell"""
        c_row, c_column = current_cell
        n_row, n_column = next_cell

        if c_column < n_column:
            self.maze[c_row][c_column][EAST] = 0
            self.maze[n_row][n_column][WEST] = 0
        elif c_column > n_column:
            self.maze[c_row][c_column][WEST] = 0
            self.maze[n_row][n_column][EAST] = 0
        elif c_row < n_row:
            self.maze[c_row][c_column][SOUTH] = 0
            self.maze[n_row][n_column][NORTH] = 0
        else:
            self.maze[c_row][c_column][NORTH] = 0
            self.maze[n_row][n_column][SOUTH] = 0

    def close_wall(self, current_cell: tuple[int, int],
                   next_cell: tuple[int, int]) -> None:
        """Close the shared wall betwenn current_cell and next_cell"""
        c_row, c_column = current_cell
        n_row, n_column = next_cell

        if c_column < n_column:
            self.maze[c_row][c_column][EAST] = 1
            self.maze[n_row][n_column][WEST] = 1
        elif c_column > n_column:
            self.maze[c_row][c_column][WEST] = 1
            self.maze[n_row][n_column][EAST] = 1
        elif c_row < n_row:
            self.maze[c_row][c_column][SOUTH] = 1
            self.maze[n_row][n_column][NORTH] = 1
        else:
            self.maze[c_row][c_column][NORTH] = 1
            self.maze[n_row][n_column][SOUTH] = 1

    def add_loops_maze(self) -> None:
        """Open loops(new paths) in the existing perfect maze to match the
           requirement perfect = False"""

        for r, row in enumerate(self.maze):
            for c, cell in enumerate(row):
                if sum(cell) == 3:
                    all_neighbours = self.get_neighbours((r, c))

                    open_neighbour: tuple[int, int] = None
                    if cell[WEST] == 0:
                        open_neighbour = (r, c - 1)
                    elif cell[EAST] == 0:
                        open_neighbour = (r, c + 1)
                    elif cell[NORTH] == 0:
                        open_neighbour = (r - 1, c)
                    elif cell[SOUTH] == 0:
                        open_neighbour = (r + 1, c)

                    closed_neighbours: list[tuple[int, int]] = []
                    for neighbour in all_neighbours:
                        if (neighbour not in self.pattern_42
                                and neighbour != open_neighbour):
                            closed_neighbours.append(neighbour)
                    random.shuffle(closed_neighbours)
                    for loop_cell in closed_neighbours:
                        self.open_wall((r, c), loop_cell)
                        if self.check_3x3_open_area():
                            self.close_wall((r, c), loop_cell)
                        else:
                            break

    def check_3x3_open_area(self) -> bool:
        """Checks if any block of 3x3 cells has all internal walls open."""

        for r, row in enumerate(self.maze):
            for c, cell in enumerate(row):
                if cell == [0, 0, 0, 0]:
                    north_open: bool = (self.maze[r - 1][c][WEST] == 0
                                        and self.maze[r - 1][c][EAST] == 0)
                    south_open: bool = (self.maze[r + 1][c][WEST] == 0
                                        and self.maze[r + 1][c][EAST] == 0)
                    west_open: bool = (self.maze[r][c - 1][NORTH] == 0
                                       and self.maze[r][c - 1][SOUTH] == 0)
                    east_open: bool = (self.maze[r][c + 1][NORTH] == 0
                                       and self.maze[r][c + 1][SOUTH] == 0)
                    if north_open and south_open and west_open and east_open:
                        return True
        return False

    def maze_solver(self) -> list[str]:
        """Find the shortest path from entry to exit.

            Returns:
                A list of cardinal direction steps
                (e.g., ['E', 'E', 'S', ...])."""
        return mockup_solution


# Format: [West (8), South (4), East (2), North (1)]
mockup_maze: list[list[list[int]]] = [
    # Row 0: [13, 8, 5, 3, 9, 3, 9, 5, 5, 3]
    [[1, 1, 0, 1], [0, 0, 0, 1], [0, 1, 0, 1], [0, 0, 1, 1], [1, 0, 0, 1], [0, 0, 1, 1], [1, 0, 0, 1], [0, 1, 0, 1], [0, 1, 0, 1], [0, 0, 1, 1]],
    # Row 1: [11, 14, 11, 10, 14, 10, 14, 9, 3, 10]
    [[1, 0, 1, 1], [0, 1, 1, 0], [1, 0, 1, 1], [1, 0, 1, 0], [1, 1, 1, 0], [1, 0, 1, 0], [1, 1, 1, 0], [1, 0, 0, 1], [0, 0, 1, 1], [1, 0, 1, 0]],
    # Row 2: [12, 3, 10, 12, 5, 2, 9, 6, 10, 10]
    [[1, 1, 0, 0], [0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0], [0, 1, 0, 1], [0, 0, 1, 0], [1, 0, 0, 1], [0, 1, 1, 0], [1, 0, 1, 0], [1, 0, 1, 0]],
    # Row 3: [9, 4, 6, 9, 3, 10, 14, 9, 6, 10]
    [[1, 0, 0, 1], [0, 1, 0, 0], [0, 1, 1, 0], [1, 0, 0, 1], [0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 1, 0], [1, 0, 0, 1], [0, 1, 1, 0], [1, 0, 1, 0]],
    # Row 4: [10, 9, 5, 6, 14, 8, 3, 10, 9, 6]
    [[1, 0, 1, 0], [1, 0, 0, 1], [0, 1, 0, 1], [0, 1, 1, 0], [1, 1, 1, 0], [1, 0, 0, 0], [0, 0, 1, 1], [1, 0, 1, 0], [1, 0, 0, 1], [0, 1, 1, 0]],
    # Row 5: [10, 10, 9, 5, 5, 6, 10, 14, 12, 3]
    [[1, 0, 1, 0], [1, 0, 1, 0], [1, 0, 0, 1], [0, 1, 0, 1], [0, 1, 0, 1], [0, 1, 1, 0], [1, 0, 1, 0], [1, 1, 1, 0], [1, 1, 0, 0], [0, 0, 1, 1]],
    # Row 6: [10, 14, 10, 9, 5, 7, 12, 5, 3, 10]
    [[1, 0, 1, 0], [1, 1, 1, 0], [1, 0, 1, 0], [1, 0, 0, 1], [0, 1, 0, 1], [0, 1, 1, 1], [1, 1, 0, 0], [0, 1, 0, 1], [0, 0, 1, 1], [1, 0, 1, 0]],
    # Row 7: [12, 3, 14, 10, 9, 5, 5, 3, 10, 14]
    [[1, 1, 0, 0], [0, 0, 1, 1], [1, 1, 1, 0], [1, 0, 1, 0], [1, 0, 0, 1], [0, 1, 0, 1], [0, 1, 0, 1], [0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 1, 0]],
    # Row 8: [11, 12, 3, 10, 14, 9, 3, 14, 8, 3]
    [[1, 0, 1, 1], [1, 1, 0, 0], [0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 1, 0], [1, 0, 0, 1], [0, 0, 1, 1], [1, 1, 1, 0], [1, 0, 0, 0], [0, 0, 1, 1]],
    # Row 9: [12, 7, 14, 12, 5, 6, 12, 5, 6, 14]
    [[1, 1, 0, 0], [0, 1, 1, 1], [1, 1, 1, 0], [1, 1, 0, 0], [0, 1, 0, 1], [0, 1, 1, 0], [1, 1, 0, 0], [0, 1, 0, 1], [0, 1, 1, 0], [1, 1, 1, 0]],
]

mockup_solution: list[str] = [
    "E", "E", "E",
    "S", "S",
    "E", "E",
    "S", "S",
    "E",
    "S", "S",
    "E", "E",
    "S", "S",
    "E",
    "S",
]
