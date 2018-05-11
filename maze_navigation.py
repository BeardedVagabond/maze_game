"""
This is a simple game in which the user navigates through a maze
The maze (for now) is static and will remain constant every time the game is launched
There are no enemies in the maze! Simply navigate your way through to find the exit
"""
import numpy as np

import maze


def print_header():
    print('=============================================')
    print()
    print("        BeardedVagabond's Maze Game")
    print()
    print('=============================================')
    print()


def initialize():
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

    # create list describing maze layout (Player begins in [0][0])
    maze_layout = [[rooms[13], rooms[3], rooms[7], rooms[0]],
                   [rooms[0], rooms[0], rooms[5], rooms[15]],
                   ]

    # verify player name input
    player_name = ''
    while not player_name:

        player_name = input('What is your name? ')

        if not player_name:
            print('Input not recognized. Please re-enter a name.\n')

    player = maze.Player(player_name, 0, 0)

    return maze_layout, player


def game_loop(maze_layout, player):
    """
    Runs the main game loop
    Reads command input from the player and responds accordingly
    :param maze_layout: list describing the layout of the maze rooms
    :param player: Player object with inputted name
    :return: UI output
    """
    while True:
        print(player.x_location, player.y_location)

        cmd = input('Do you wish to [M]ove, [L]ook around, or E[x]it? ')
        if not cmd:
            print("No input detected, please re-enter a command\n")
            continue

        cmd = cmd.lower().strip()

        if cmd == 'm':
            move = 0

            while not move:
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

        elif cmd == 'l':
            player.look(maze_layout[player.y_location][player.x_location])
            print()

        elif cmd == 'x':
            print('Thanks for playing!')
            break

        else:
            print(f"I'm sorry, {cmd} was not recognized. Please re-enter a command.\n")

        if player.x_location == 3 and player.y_location == 1:
            print(f'{player.name} has made it to the end of the maze! Congratulations!!')
            print("'Thanks for playing!")
            break


def main():
    """
    Contains function calls in order required to execute the game
    :return: Standard 0 for completion and 1 for error
    """
    print_header()
    maze_layout, player = initialize()
    game_loop(maze_layout, player)


if __name__ == '__main__':
    main()
