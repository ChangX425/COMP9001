'''
game.py — Space Exploration Game Module

The game module runs the space exploration game.

It coordinates gameplay by integrating the map functionality from space_map.py
and the Ship class from ship.py. This module initialises the space exploration
map and ship, and runs the game where players issue commands to explore the 
map, interact with entities, and aim to reach the destination.
'''

# import your 2 files here!
import ship
import space_map

def main():
    '''
    Runs the entire program from start to end. 
    
    All program logic must be executed within the main() function. We have
    provided some starting implementation and comments to help you out.
    '''
    print('>>> STARTING ROUTE: Kepler-452b -> Sector 9-Delta\n')

    # 1. Configuring navigation systems
    print('>> CONFIGURING NAVIGATIONAL SYSTEMS')

    # - Ask for size of map
    while True:
        n = int(input(f'Enter size of map (n >= 2): '))
        if n < 2:
            print('Error: n too low')
        else:
            print(f'{n} x {n} map initialised.\n')
            break

    # - Then use this size to create a map reusing functions from the space_map 
    #   module!
    grid = space_map.create_map(n)
    space_map.populate_map(grid)
    print(f'>> NAVIGATIONAL SYSTEMS READY\n')

    # 2. Configuring ship systems
    print(f'>> CONFIGURING SHIP SYSTEMS')

    ship_name = input(f'Enter ship name: ')

    while True:
        fuel_amount = int(input(f'Enter fuel (1-99): '))
        if fuel_amount <= 0:
            print(f'Error: fuel too low')
        elif fuel_amount > 99:
            print(f'Error: fuel too high')
        else:
            break
    
    user_ship = ship.Ship(ship_name, fuel_amount)
    print(user_ship)        # return def __str__
    print('>> SHIP SYSTEMS READY\n')
    print(f">>> EXECUTING LIFTOFF: EXITING Kepler-452b's ORBIT\n")
    # - Ask for name and fuel of ship
    # - Then using the name and fuel, create a Ship instance reusing the Ship
    #   class from the ship module!
    # ...

    print('>>> AWAITING COMMANDS\n')
    # 3. Game Loop
    while True:
        commands = input(f'Enter (n,e,s,w | map | status): ')
        if commands == 'q':
            grid[user_ship.y][user_ship.x] = 'L'
            print(f'{user_ship.name} has self-destructed.')
            space_map.display_map(grid)
            print(f'\n>>> MISSION FAILED')
            break

        if commands not in {'map', 'status', 'n', 'e', 's', 'w', 'q'}:
            print('Error: unrecognised command')
            continue
        if commands == 'map':
            space_map.display_map(grid)
            continue
        if commands == 'status':
            print(user_ship)
            continue

        xx = 0
        yy = 0  #set initial coords

        if commands == 'n':
            yy -= 1
        elif commands == 'e':
            xx += 1
        elif commands == 's':
            yy += 1
        elif commands =='w':
            xx -= 1
        
        current_x = user_ship.x + xx
        current_y = user_ship.y + yy

        if not (0 <= current_x < n and 0 <= current_y < n):
            print(f'Error: out of bounds')
            continue

        symbol = grid[current_y][current_x]
        moved = user_ship.interact(symbol, current_x, current_y)

        if moved:
            if symbol == 'X':
                grid[current_y][current_x] = 'W'
                grid[current_y - yy][current_x - xx] = ' '
                space_map.display_map(grid)
                print(f'\n>>> MISSION COMPLETED')
                break
            
            elif user_ship.is_out_of_health():
                grid[current_y][current_x] = 'L'
                grid[current_y - yy][current_x - xx] = ' '
                space_map.display_map(grid)
                print('\n>>> MISSION FAILED')
                break
            
            else:
                grid[current_y][current_x] = '@'
                grid[current_y - yy][current_x - xx] = ' '

            if user_ship.is_out_of_fuel():
                grid[current_y][current_x] = 'L'
                print(f'{user_ship.name} is out of fuel.')
                space_map.display_map(grid)
                print('\n>>> MISSION FAILED')
                break

    # - At this stage, you should have both a map and ship initialised
    # - Take in commands from user to navigate map and progress the game
    # - You'll need to make frequent use of both your map and ship!
    #    - Your ship stores (x, y): This is [y][x] on the map!
    #    - When you find where the ship wants to move, call its interact()
    #      method!
    # - After each interaction, you'll need to check win/loss conditions
    #    - Check if ship reached destination (remember ship stores this!)
    #    - Check if ship has no health
    #    - Check if ship has no fuel left
    # ...


# don't modify this!
if __name__ == '__main__':
    main()
