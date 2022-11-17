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

def create_grid():
"""Create grid and randomly place ships in different directions"""   


def show_grid():
"""Will show the grid with rows A-J and columns 0-9"""
