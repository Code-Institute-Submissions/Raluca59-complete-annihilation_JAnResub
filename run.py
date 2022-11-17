import random
import time

# Global variable for grid
grid = [[]]
# Global variable for grid size
grid_size = 10
# Global variable for ships
numb_ships = 3
# Global variable for ships sunk 
ships_sunk = 0
# Global variable for bullets 
bullets_left = 60
# Global variable for ship position
ship_position = [[]]
# Global variable for game status
game_over = False
# Global variable for alphabet
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
            for c in range(start_col, end_col):
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
        row = []
        for c in range(cols):
            row.append(".")
        grid.append(row)
    numb_placed_ships = 0
    ship_position = []

    while numb_placed_ships != numb_ships:
        random_row = random.randint(0, rows - 1)
        random_col = random.randint(0, cols - 1)
        direction = random.choice(["left", "right", "up", "down"])
        ship_size = random.randint(3, 5)
        if place_ship_on_grid(random_row, random_col, direction, ship_size):
            numb_placed_ships += 1

def show_grid():
    """Will show the grid with rows A-J and columns 0-9"""
    global grid
    global alphabet

    debug_mode = True
    alphabet = alphabet[0: len(grid) + 1]
    for row in range(len(grid)):
        print(alphabet[row], end= " ")
        for col in range(len(grid[row])):
            if grid[row][col] == "O":
                if debug_mode:
                    print("O", end=" ")
                else:
                    print(".", end=" ")    
            else:
                print(grid[row][col], end=" ")        
        print("")        
    print(" ", end=" ")
    for i in range(len(grid[0])):
        print(str(i), end=" ")
    print("")


def valid_bullet_coordinate():
    """Checks if coordinates of the bullet is valid"""

    global grid
    global alphabet

    is_valid_coordinate = False
    row = -1
    col = -1

    while is_valid_coordinate is False:
        coordinate = input("Enter row (A-J) and column (0-9): ")
        coordinate = coordinate.upper()
        if len(coordinate) <= 0 or len(coordinate) > 2:
            print("Please enter only one row and one column.")
            continue
        row = coordinate[0]
        col = coordinate[1]
        if not row.isalpha() or not col.isnumeric():
            print("Please enter a letter between A-J and a number between 0-9.")
            continue
        row = alphabet.find(row)
        if not (-1 < row < grid_size):
            print("Please enter a letter between A-J and a number between 0-9.")
            continue
        col = int(col)
        if not (-1 < col < grid_size):
            print("Please enter a letter between A-J and a number between 0-9.")
            continue
        if grid[row][col] == "#" or grid[row][col] == "X":
            print("You have already shot a bullet at this location. Try another!")
            continue
        if grid[row][col] == "." or grid[row][col] == "O":
            is_valid_coordinate = True

    return row, col


def check_sunken_ships(row, col):
    """Checks if all parts of a ship have been hit and iterates the number of ships sunk"""

    global grid
    global ship_position

    for position in ship_position:
        start_row = position[0]
        end_row = position[1]
        start_col = position[2]
        end_col = position[3]
        if start_row <= row <= end_row and start_col <= col <= end_col:
            for r in range(start_row, end_row):
                for c in range(start_col, end_col):
                    if grid[r][c] != "X":
                        return False

    return True


def shoot():
    """Updates the grid whenever a bullet is shot"""

    global grid
    global ships_sunk
    global bullets_left

    row, col = valid_bullet_coordinate()
    print("")
    print("--------------------")

    if grid[row][col] == ".":
        print("You missed! No ship at this position.")
        grid[row][col] = "#"
    elif grid[row][col] == "O":
        print("You hit a ship!")
        grid[row][col] = "X"
        if check_sunken_ships(row, col):
            print("A ship was destroyed!")
            ships_sunk +=1
        else:
            print("A ship was damaged!")

    bullets_left -= 1



def play():
    """Main entry for game loop"""
    global game_over

    create_grid()
    show_grid()
    confirm_grid_place_ship()
    place_ship_on_grid()

    print("-------Complete Annihilation")

play()