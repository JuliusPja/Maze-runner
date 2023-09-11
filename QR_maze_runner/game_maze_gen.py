import random
import pygame 
pygame.init()


class Maze: 
    # Constructor to initialize the maze properties
    def __init__(self, width, height, wall_density=0.4):
        self.width = width
        self.height = height
        # Generate the maze layout using random walls
        self.maze_layout = [['#' if random.random() < wall_density else ' ' for _ in range(width)] for _ in range(height)]
        self.start_pos = (0, height - 1)   
        self.exit_pos = (width - 1, 0)
        self.treasure_pos = None
        self.treasure_placed = False
        self.wall_density = wall_density

    # Method to display the maze layout
    def display_maze(self):
        for row in self.maze_layout:
            print(''.join(str(cell) for cell in row))

    # Check if the given position is the exit position
    def is_exit(self, x, y):
        return (x, y) == self.exit_pos
    
    # Check if the given position contains the treasure
    def is_treasure_pos(self, x, y):
        return (x, y) == self.treasure_pos  
    
    # Check if the given position is valid (within the maze boundaries) 
    def is_valid(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height
    
    # Check if the given position is a wall
    def is_wall(self, x, y):
        return self.maze_layout[y][x] == '#'



# the Depth-First Search (DFS) algorithm, where we start generating the maze from the player's 
# starting position and ensure that we connect all the cells of the maze during the generation process.
    
    def generate_maze(self):

        # Pick a random starting cell for the maze
        start_x, start_y = random.randint(0, self.width - 1), random.randint(0, self.height - 1)

        # The starting cell is part of the maze
        self.maze_layout[start_y][start_x] = ' '
        visited = {(start_x, start_y)}

        # List of walls that can be expanded to grow the maze
        walls = [(start_x + dx, start_y + dy) for dx, dy in [(0, -2), (0, 2), (-2, 0), (2, 0)]]

        
        while walls:
            x, y = random.choice(walls)

            # Get the neighboring cells of the wall
            neighbors = [(x + dx, y + dy) for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)] if 0 <= x + dx < self.width and 0 <= y + dy < self.height]

            # Count the number of neighboring cells that are already part of the maze
            num_visited_neighbors = sum(1 for nx, ny in neighbors if (nx, ny) in visited)


            if num_visited_neighbors == 1:
                # If exactly one neighboring cell is part of the maze, make the wall part of the maze
                self.maze_layout[y][x] = ' '
                visited.add((x, y))

                # Add the neighboring walls of the newly added cell to the walls list
                for nx, ny in neighbors:
                    if (nx, ny) not in visited:
                        walls.append((nx, ny))

            walls.remove((x, y))

    # Get a random valid location to place the treasure ('T') in the maze
    def get_random_valid_location(self):
        if not self.treasure_placed:
            # Get a list of all valid positions (not walls, exit, or player start)
            valid_positions = [(x, y) for y in range(self.height) for x in range(self.width)
                            if (x, y) != self.exit_pos and (x, y) != self.start_pos and not self.is_wall(x, y)]

            # Pick a random position from the list of valid positions
            self.treasure_pos = random.choice(valid_positions)
            self.treasure_placed = True
        
        return self.treasure_pos