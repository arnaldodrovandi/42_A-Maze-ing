from maze_generator import MazeGenerator

def main() -> None:
    maze1 = MazeGenerator(20, 15, (0,0), (19,14), "output.txt", False)
    print(maze1.generate_maze_perfect())
    print("\nShortest path:\n", maze1.maze_solver())

if __name__ == "__main__":
    main()