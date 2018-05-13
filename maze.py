class Room:
    def __init__(self, doors, size):
        self.doors = doors  # 1/0 pseudo-boolean list of [North, East, South, West] openings
        self.size = size  # string for small, medium, large (mainly for future implementation)

    def __str__(self):
        openings = []
        if self.doors[0]:
            openings.append('North')

        if self.doors[1]:
            openings.append('East')

        if self.doors[2]:
            openings.append('South')

        if self.doors[3]:
            openings.append('West')
        openings = ', '.join(openings[:-2] + [', and '.join(openings[-2:])])

        return f'The {self.size} room has {openings} doors.' if openings else f'Empty room!'


class Player:
    def __init__(self, name, x_location, y_location):
        self.name = name
        self.x_location = x_location
        self.y_location = y_location

    def __str__(self):
        return f'An adventurer named {self.name}.'

    def move(self, direction, maze_layout):
        """
        Moves the player into a new room if possible
        :param direction: string for north, east, south, west (first letter only)
        :param maze_layout: the maze_layout list housing the full structure
        :return: 1 for successful move, 0 otherwise (NOTE: player will also move location when applicable)
        """

        room = maze_layout[self.y_location][self.x_location]

        if direction == 'n' and room.doors[0]:  # North attempt
            self.y_location -= 1
            return 1

        elif direction == 'e' and room.doors[1]:  # East attempt
            self.x_location += 1
            return 1

        elif direction == 's' and room.doors[2]:  # South attempt
            self.y_location += 1
            return 1

        elif direction == 'w' and room.doors[3]:  # West attempt
            self.x_location -= 1
            return 1

        else:
            compass = 'north' if direction == 'n' else \
                'east' if direction == 'e' else \
                    'south' if direction == 's' else 'west'
            print(f'{self.name} walks into a wall when attempting to move {compass}\n')
            return 0

    def look(self, room):
        """
        Looks at the current room and lists doors
        :param room: current room object
        :return: UI output
        """

        print(f'{self.name} looks around the room...')
        print(room)

    def check_map(self, maze_choice):
        """
        checks maps to see current location
        :param maze_choice: index of room chosen
        :return: UI output
        """

        print(f'{self.name} checks their map...')
        print(f'Your current coordinates are ({self.x_location}, {self.y_location}) in Maze #{maze_choice+1}.')
