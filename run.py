import random
import time

#Global variable for grid
grid = [[]]
#Global variable for grid size
grid_size = 10
#Global variable for ships
numb_ships = 3
#global variable for ships sunk 
ships_sunk = 0
#Global variable for bullets 
bullets_left = 60
#Global variable for ship position
ship_position = [[]]
#Global variable for game status
game_over = False
#Global variable for alphabet
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def confirm_grid_place_ship(start_row, end_row, start_col, end_col):
"""Check the row or column to see if is safe to place the ship"""
    global grid
    global ship_position

    all_confirmed = True
    for r in range(start_row, end_row):
        for c in range(start_col, end_col):
            if grid[r][c] != ".":
                all_confirmed = False
                break
    if all_confirmed:
        ship_position.append([start_row, end_row, start_col, end_col])
        for r in range(start_row, end_row):
            for c in ramge(start_col, end_col):
                grid[r][c] = "O"
    return all_confirmed


def place_ship_on_grid(row, col, direction, length):
"""Try to place a ship on grid based on direction"""
global grid_size

start_row, end_row, start_col, end_col = row, row + 1, col, col + 1
if direction == "left":
    if col - length < 0:
        return False
    start_col = col - length + 1    
elif direction == "right":
    if col + length >= grid_size:
        return False
    end_col = col + length
elif direction == "up":
    if row - length < 0:
        return False
    start_row = row - length + 1
elif direction == "down":
    if row + length >= grid_size:
        return False
    end_row = row + length
return confirm_grid_place_ship(start_row, end_row, start_col, end_col)




def create_grid():
"""Create grid and randomly place ships in different directions"""
global grid
global grid_size
global numb_ships
global ship_position

random.seed(time.time())
rows, cols = (grid_size, grid_size)

grid = []
for r in range(rows):
    rows = []
    for c in range(cols):
        row.append(".")
    grid.append(row)
numb_placed_ships = 0
ship_position = []

while numb_placed_ships != numb_ships:
    random_row = random.randint(0, rows - 1)
    random_col = random.randint(0, col - 1)
    direction = random.choice(["left", "right", "up", "down"])
    ship_size = random.randint(3, 5)
    if place_ship_on_grid(random_row, random_col, direction, ship_size):
        numb_placed_ships += 1

def show_grid():
"""Will show the grid with rows A-J and columns 0-9"""
