"""
This is a simple game in which the user navigates through a maze
The maze will be chosen at random from three options
I've never made a maze before... so the relative difficult is pretty random
First maze has a couple loops
Second maze is the largest and has no loops
Third maze is the smallest and has no loops
Fourth maze is generated using the function random_maze (loops possible, quality not ensured)
There are no enemies in the maze! Simply navigate your way through to find the exit
"""
import random
import numpy as np

import maze

# todo: need a way to visualize mazes other than transcribing by hand...

def print_header():
    print('=============================================')
    print()
    print("        BeardedVagabond's Maze Game")
    print()
    print('=============================================')
    print()


def initialize():
    """
    Creates the maze_layout list of rooms and the player object
    :return: maze_choice, maze_layout, player
    """

    # create all possible rooms
    rooms = [maze.Room([0, 0, 0, 0], 'small'),  # Closed room(0)
             maze.Room([1, 1, 1, 1], 'small'),  # Open room(1)
             maze.Room([1, 0, 1, 0], 'small'),  # NS corridor(2)
             maze.Room([0, 1, 0, 1], 'small'),  # EW corridor(3)
             maze.Room([1, 0, 0, 1], 'small'),  # NW corner(4)
             maze.Room([1, 1, 0, 0], 'small'),  # NE corner(5)
             maze.Room([0, 1, 1, 0], 'small'),  # SE corner(6)
             maze.Room([0, 0, 1, 1], 'small'),  # SW corner(7)
             maze.Room([1, 1, 0, 1], 'small'),  # EW with N tee(8)
             maze.Room([1, 1, 1, 0], 'small'),  # NS with E tee(9)
             maze.Room([0, 1, 1, 1], 'small'),  # EW with S tee(10)
             maze.Room([1, 0, 1, 1], 'small'),  # NS with W tee(11)
             maze.Room([1, 0, 0, 0], 'small'),  # N dead end(12)
             maze.Room([0, 1, 0, 0], 'small'),  # E dead end(13)
             maze.Room([0, 0, 1, 0], 'small'),  # S dead end(14)
             maze.Room([0, 0, 0, 1], 'small'),  # W dead end(15)
             ]

    # create list using room indexes (will be converted when chosen)
    maze_1 = [[13, 3, 10, 7, 14, 0, 0],
              [13, 3, 4, 5, 11, 0, 0],
              [6, 7, 6, 3, 8, 7, 0],
              [2, 5, 1, 3, 15, 2, 0],
              [5, 3, 12, 7, 6, 4, 0],
              [0, 0, 0, 5, 11, 0, 0],
              [0, 0, 0, 0, 5, 3, 15],
              ]

    maze_2 = [[13, 10, 3, 3, 7, 14, 0, 14, 0, 0, 0],
              [0, 2, 13, 3, 4, 2, 0, 2, 0, 0, 0],
              [0, 5, 10, 3, 7, 2, 0, 9, 3, 3, 7],
              [0, 13, 4, 6, 8, 4, 14, 12, 14, 0, 2],
              [0, 0, 6, 8, 3, 7, 2, 0, 5, 3, 11],
              [0, 13, 1, 3, 7, 12, 2, 6, 7, 13, 11],
              [0, 0, 2, 14, 5, 3, 8, 11, 5, 3, 4],
              [0, 0, 5, 4, 0, 13, 3, 4, 0, 0, 0],
              ]

    maze_3 = [[13, 3, 7, 13, 7, 0, 14],
              [14, 13, 8, 7, 2, 0, 2],
              [2, 6, 7, 5, 8, 7, 2],
              [5, 4, 5, 3, 3, 8, 4],
              ]

    maze_4 = random_maze(10)

    # create list of mazes, choose random maze for game, convert maze indexes to rooms
    mazes = [maze_1, maze_2, maze_3, maze_4]
    maze_choice = random.choice(range(0, 3))
    maze_layout = mazes[maze_choice]
    maze_layout = index_to_rooms(maze_layout, rooms)

    # verify player name input
    player_name = ''
    while not player_name:

        player_name = input('What is your name? ')

        if not player_name:
            print('Input not recognized. Please re-enter a name.\n')

    player = maze.Player(player_name, 0, 0)

    return maze_choice, maze_layout, player


def random_maze(size):
    """
    Creates a random square maze of dimension = size
    :param size: Square dimension of desired maze
    :return: A list describing a random maze using index format
    """

    # Pad maze with 0 with zero index perimeter
    size += 2
    new_maze = np.empty((size, size))
    new_maze[0, :] = np.zeros((1, size))
    new_maze[-1, :] = np.zeros((1, size))
    new_maze[:, 0] = np.zeros(size)
    new_maze[:, -1] = np.zeros(size)

    # Define possible indexes for each compass direction
    north = [1, 2, 4, 5, 8, 9, 11, 12]
    east = [1, 3, 5, 6, 8, 9, 10, 13]
    south = [1, 2, 6, 7, 9, 10, 11, 14]
    west = [1, 3, 4, 7, 8, 10, 11, 15]

    # Set starting position
    new_maze[1][1] = 13

    # Loop through by row ensuring room connections
    for i in range(1, size - 1):

        for j in range(0, size - 2):
            # Determine if a connection is needed to adjacent rooms
            left_door = 1 if new_maze[i][j] in east else 0
            top_door = 1 if new_maze[i - 1][j + 1] in south else 0
            # bottom_door = 1 if new_maze[i + 1][j + 1] in north else 0
            # right_door = 1 if new_maze[i][j + 1] in west else 0

            if i < size - 2:  # for all rows above bottom row of actual maze

                if j < size - 3:  # for all columns before rightmost of actual maze

                    # Choose room at random that will connect with adjacent rooms
                    if left_door:
                        if top_door:
                            options = list(set(west) & set(north))

                        else:
                            options = list(set(west) - set(north))
                    else:
                        if top_door:
                            options = list(set(north) - set(west))

                        else:
                            options = list((set(south) & set(east)) - set(north) - set(west))

                else:

                    # Right edge of maze... can never go east
                    if left_door:
                        if top_door:
                            options = list((set(west) & set(north)) - set(east))

                        else:
                            options = list((set(west) - set(north)) - set(east))
                    else:
                        if top_door:
                            options = list(set(north) - set(west) - set(east))

                        else:
                            options = list(set(south) - set(north) - set(west) - set(east))

            else:  # Bottom edge of maze... can never go south

                if j < size - 3:  # for all columns before rightmost of actual maze

                    if left_door:
                        if top_door:
                            options = list((set(west) & set(north)) - set(south))

                        else:
                            options = list((set(west) - set(north)) - set(south))
                    else:
                        if top_door:
                            options = list(set(north) - set(west) - set(south))

                        else:
                            options = list(set(east) - set(west) - set(north) - set(south))

                else:
                    # Bottom right corner... can only go west and north
                    if left_door:
                        if top_door:
                            options = list((set(west) & set(north)) - set(south) - set(east))

                        else:
                            options = list((set(west) - set(north)) - set(south) - set(east))
                    else:
                        if top_door:
                            options = list(set(north) - set(west) - set(south) - set(east))

                        else:
                            options = [0]

            if i == 1 and j == 1:
                new_maze[1][1] = 13  # enforce starting position
                new_maze[i][j + 1] = random.choice(options)
            else:
                new_maze[i][j + 1] = random.choice(options)

    # Extract actual maze
    new_maze = new_maze[1:-1, 1:-1]
    return new_maze


def index_to_rooms(maze_x, rooms):
    """
    This function replaces maze lists of indexes with room objects
    :param maze_x: Maze to be recast into rooms
    :param rooms: List of possible rooms
    :return: List describing maze layout with room objects
    """
    i = 0
    for x in maze_x:
        j = 0

        for y in x:
            maze_x[i][j] = rooms[y]
            j += 1

        i += 1

    return maze_x


def game_loop(maze_choice, maze_layout, player):
    """
    Runs the main game loop
    Reads command input from the player and responds accordingly
    :param maze_choice: int index of which maze was chosen
    :param maze_layout: list describing the layout of the maze rooms
    :param player: Player object with inputted name
    :return: UI output
    """

    while True:

        cmd = input('Do you wish to [M]ove, [L]ook around, [C]heck map, or E[x]it? ')
        if not cmd:
            print("No input detected, please re-enter a command\n")
            continue

        cmd = cmd.lower().strip()

        if cmd == 'm':
            move = 0

            while not move:
                move = move_loop(maze_layout, move, player)

        elif cmd == 'l':
            player.look(maze_layout[player.y_location][player.x_location])
            print()

        elif cmd == 'x':
            print('Thanks for playing!')
            break

        elif cmd == 'c':
            player.check_map(maze_choice)
            print()

        else:
            print(f"I'm sorry, {cmd} was not recognized. Please re-enter a command.\n")

        # Set and check end of maze condition
        x_finish = 6 if maze_choice == 0 else 7 if maze_choice == 1 else 0
        y_finish = 6 if maze_choice == 0 else 0 if maze_choice == 1 else 1

        if player.x_location == x_finish and player.y_location == y_finish:
            print(f'{player.name} has made it to the end of the maze! Congratulations!!')
            print("'Thanks for playing!")
            break


def move_loop(maze_layout, move, player):
    print('Where would you like to move?')

    direction = ''
    while not direction:
        direction = input('[N]orth, [E]ast, [S]outh, [W]est: ')

        if not direction:
            print("No input detected, please re-enter a direction\n")
            continue

    direction = direction.lower().strip()

    if direction == 'n':
        move = player.move(direction, maze_layout)
        if move:
            print(f'{player.name} moves north into the next room\n')

    elif direction == 'e':
        move = player.move(direction, maze_layout)
        if move:
            print(f'{player.name} moves east into the next room\n')

    elif direction == 's':
        move = player.move(direction, maze_layout)
        if move:
            print(f'{player.name} moves south into the next room\n')

    elif direction == 'w':
        move = player.move(direction, maze_layout)
        if move:
            print(f'{player.name} moves west into the next room\n')

    else:
        print(f"Sorry, the command {direction} was not recognized. Please re-enter a command.\n")

    return move


def main():
    """
    Contains function calls in order required to execute the game
    :return: Standard 0 for completion and 1 for error
    """

    print_header()
    maze_choice, maze_layout, player = initialize()
    game_loop(maze_choice, maze_layout, player)


if __name__ == '__main__':
    main()
