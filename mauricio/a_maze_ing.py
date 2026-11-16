"""Main entry point of the A-Maze-ing project."""

import sys


def get_config_file_name(arguments: list[str]) -> str:
    """Check the command line arguments and return the config file name.

    Args:
        arguments: The list of command line arguments (sys.argv).

    Returns:
        The name of the configuration file given by the user.

    Raises:
        ValueError: If the number of arguments is not exactly two.
    """
    if len(arguments) != 2:
        raise ValueError("Usage: python3 a_maze_ing.py config.txt")
    return arguments[1]


def main() -> None:
    """Run the maze program."""
    try:
        config_file_name = get_config_file_name(sys.argv)
    except ValueError as error:
        print(f"Error: {error}")
        sys.exit(1)
    print(f"Config file received: {config_file_name}")


if __name__ == "__main__":
    main()
