class MazeGenerator:
    """Generate and solve mazes.
    
    Attributes:
        width: Maze's number of columns.
        height: Maze's number of rows.
        entry: Start point (x, y) in the Maze.
        exit: Final point (x, y) in the Maze.
        output_file: Output file name.
        perfect: Generate a perfect Maze(only one path from entry to exit) if True, and a Maze with multiple paths if False.
        seed: Optional seed to control randomness by producing the exact same Maze every time. """
    def __init__(self, width: int, height: int, entry: tuple[int, int], 
                 exit: tuple[int, int], output_file: str, perfect: bool,
                 seed: int|None = None ) -> None:
        self.width = width
        self.height = height
        self.entry = entry
        self.exit = exit
        self.output_file = output_file
        self.perfect = perfect
        self.seed = seed

    def closed_grid_gen(self) -> list:
        """Generate an initial grid with all four walls closed for each cell.
        Returns:
            A 3D list where each cell is [West, South, East, North] = [1,1,1,1].
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
        """Generate a maze with only one path from entry point to exit point(perfect maze).
            
            Returns:
                A matrix list where every row is a list of cells and every cell is
            represented by 4 integers [West, South, East, North] (1=closed,
            0=open).
                """
        # maze: list = self.closed_grid_gen()
        return mockup_maze

    def blocked_42(self) -> None:
        """Mark the "42" pattern in the center as "visited" to keep its four walls closed"""
        pass

    def add_loops_maze(self) -> None:
        """Open loops(new paths) in the existing perfect maze to match the requirement perfect = False"""
        pass

    def maze_solver(self) -> list[str]:
        """Find the shortest path from entry to exit.
        
            Returns:
                A list of cardinal direction steps (e.g., ['E', 'E', 'S', ...])."""
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