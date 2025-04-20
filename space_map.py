'''
space_map.py — Space Exploration Map Module

This module provides the core functionality for creating and managing a
space exploration map in the space exploration game. 

It allows users to initialise a map, display it and populate it with key 
entities including the ship, destination, hazards and waypoints.
'''


def create_map(n: int) -> list[list[str]]:
    empty_map = []
    for _ in range(n): #set range(n) to make the map change it scale by n
        empty_map.append([' '] * n)
    return empty_map

    '''
    Initialises and returns an n x n grid representing the game map.

    Parameters:
        n (int): The size of the grid (number of rows and columns).

    Returns:
        list[list[str]]: A 2D list representing the game map.
    '''

def display_map(grid: list[list[str]]):
    '''
    Prints the current state of the grid in a readable map format.

    Parameters:
        grid (list[list[str]]): The 2D list representing the game map.
    '''
    for row in grid: 
        line = '|'
        for cell in row: 
            line += ' ' +cell + ' ' + '|'
        print(line)


def populate_map(grid: list[list[str]]):
    '''
    Populates the grid with key entities including the ship, destination,
    hazards, and waypoints.

    Note: Coordinate (x, y) cooresponds to grid[y][x].

    Parameters:
        grid (list[list[str]]): The 2D list representing the game map.
    '''
    #step 1
    i = len(grid) # set the bound that can check whether user input is out of the bound
    print('Placing: Ship\nShip placed: (0, 0)')
    grid[0][0] = '@'
    display_map(grid)

    #step 2
    print('\nPlacing: Destination')

    while True:
        coords = input('Enter (x y): ')
        split = coords.split()
        if len(split) != 2:
            print('Error: expected <x> <y>')
            continue

        try:
            x, y = map(int, split)
        except ValueError:
            print("Error: expected <x> <y>")
            continue
        
        if not (0 <= x < i and 0 <= y < i):
            print('Error: out of bounds')
            continue
        
        if x == 0 and y == 0:
            print("Error: (0, 0) occupied by '@'")
            continue
        grid[y][x] = 'X' #Coordinate (x, y) cooresponds to grid[y][x] Interesting!
        print(f'Destination placed: ({x}, {y})')
        display_map(grid)
        break

    #step 3!
    print('\nPlacing: Hazards and Waypoints')
    while True:
        coords2 = input('Enter (symbol x y | display | done): ')
        split2 = coords2.split()
        if coords2 == 'display':
            display_map(grid)
            continue

        if coords2 == 'done':
            display_map(grid)
            break

        if len(split2) != 3:
            print('Error: expected <symbol> <x> <y>')
            continue

        symbol = split2[0]
        try:
            a = int(split2[1])
            b = int(split2[2])
        except ValueError:
            print("'Error: expected <symbol> <x> <y>'")
            continue


        if symbol not in {'.', 'E', 'M', 'R'}:
            print(f"Error: '{symbol}' not recognised")
            continue

        if not (0 <= a < i and 0 <= b < i):
            print('Error: out of bounds')
            continue

        if grid[b][a] != ' ':
            print(f"Error: ({a}, {b}) occupied by '{grid[b][a]}'")

        else:
            if symbol == 'M':
                grid[b][a] = symbol
                print(f'Mineral placed: ({a}, {b})')
                continue

            if symbol == 'E':
                grid[b][a] = symbol
                print(f'Enemy placed: ({a}, {b})')
                continue

            if symbol == '.':
                grid[b][a] = symbol
                print(f'Asteroid placed: ({a}, {b})')
                continue
            if symbol == 'R':
                grid[b][a] = symbol
                print(f'Repair Station placed: ({a}, {b})')
                continue
    

if __name__ == '__main__':
    print(create_map(5))
    print(display_map(empty_map))
    # this only runs when its the main program ran i.e. python3 space_map.py
