# maze_navigation
A text-based maze navigation game with randomly selected mazes from a collection of three

NOTE: Originally coded in PyCharm using a Conda environment (Python 3.6)
      

Game consists of two files: 1. bv_maze_navigation.py and 2. maze.py
1. bv_maze_navigation.py contains all functions and UI output required to run the main game loop
2. actors.py is imported as a module to bv_maze_navigation.py and includes all required classes to create mazes and player object

The game consists of easy to read console output and prompts that guide the user through several phases:
    
1. Maze Instantiation
	a. This phase is completed "behind the scenes" with no input from the player
	b. First every possible room object is created
		- i.e. a room with each combination of compas direction doors
	c. Mazes are created as a list with numerical indexes for room types
		- mazes were hand drawn and transcribed to room indexes
	d. Next, one of three mazes are chosen at random for the game instance
	e. Finally, a nested for loop converts the chosen map from indexes to room objects

2. Player instantiation
	a. Name input is verified to be a string before continuing, however, any string input will be accepted
	b. Once a name is accepted, the palyer object is instantiated at location (0, 0)
        
3. Main game loop
	a. Command input
		- Possible commands are: [M]ove, [L]ook around, [C]heck map, or E[x]it
		- Commands are made thrugh hinted character input
		- Sring input is processed using lower() and strip() methods to simplify selection
		- A blank input yields a no input message before looping
		- Invalid string input tields a message stating the string is not recognized before looping
	b. Move
		- This commands attempts to move the palyer in the selected compas direction
		- Input is verified both to exist (or error message) and be a compass direction (or error message)
		- When a compass direction is selected, the room is checked to have a coresponding open door
		- If the door exists, the player is moved into the next room accordingly and the move loop breaks
		- If the door does not exist, the player walks into a wall and must choose another direction
		- Loops until a valid selection is made
	c. Look Around
		- This command lists the directions with an open door in the current room
	d. Check Map
		- This command lists the current player coordinates as well as the current maze being navigated
	e. Exit
		- This command simply exits the game with a "Thanks for playing" message
	- NOTE: If the player reaches the end of the maze, the main loop will end printing a congratulatory message and exiting the game

