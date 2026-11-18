from maze_generator import MazeGenerator

def main() -> None:
    maze1 = MazeGenerator(20, 20, (13,7), (19,14), "output.txt", True)
    print(maze1.generate_maze_perfect())
    print("\nShortest path:\n", maze1.maze_solver())

if __name__ == "__main__":
    main()