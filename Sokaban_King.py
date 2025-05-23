'''
No use outside of python built_in libraries
Haven't use anything cannot be run on Ed
'''

levels = [
    [
        list("########"),
        list("#@     #"),
        list("#  $   #"),
        list("#     .#"),
        list("########")
    ],
    [
        list("#######"),
        list("#@    #"),
        list("#   $ #"),
        list("# $$  #"),
        list("#  .  #"),
        list("# ..  #"),
        list("#######")
    ],
    [
        list("########"),
        list("#@     #"),
        list("# $$ $ #"),
        list("# $..  #"),
        list("#  ..  #"),
        list("########")
    ]
]

def find_player(game_map):
    for y, row in enumerate(game_map):
        for x, cell in enumerate(row):
            if cell == '@' or cell == '+':
                return x, y
    return -1, -1

def print_map(game_map):
    for row in game_map:
        print("".join(row))

def move(game_map, dx, dy):
    x, y = find_player(game_map)
    nx, ny = x + dx, y + dy
    nnx, nny = x + 2*dx, y + 2*dy

    current = game_map[y][x]
    target = game_map[ny][nx]

    # Move from start space
    game_map[y][x] = '.' if current == '+' else ' '

    # Move to blank space or target
    if target in ' .':
        game_map[ny][nx] = '+' if target == '.' else '@'

    # if is case
    elif target in '$*':
        next_target = game_map[nny][nnx]
        if next_target in ' .':
            # move the case
            game_map[nny][nnx] = '*' if next_target == '.' else '$'
            game_map[ny][nx] = '+' if target == '*' else '@'

def win(game_map):
    for row in game_map:
        if '.' in row or '+' in row:
            return False
    return True

def play():
    print('''Sokoban start! Use W A S D control direction, press Q to exit the game

Remember! There is no way back!(Don't know how to do it OvO)
So think carefully before you move!
''')
    for level_num, level_map in enumerate(levels):
        game_map = [row[:] for row in level_map]
        print(f"\n--- Level {level_num + 1}  ---")
        while True:
            print_map(game_map)
            cmd = input("Next step (w/a/s/d): ").lower()
            if cmd == 'q':
                print("Game exited")
                return
            elif cmd in 'wasd':
                direction = {'w': (0, -1), 'a': (-1, 0), 's': (0, 1), 'd': (1, 0)}
                dx, dy = direction[cmd]
                move(game_map, dx, dy)
                if win(game_map):
                    print_map(game_map)
                    print("You have moved one step forward to become Sokoban King!")
                    break
            else:
                print("Invalid command, please use W A S D control direction, press Q to exit the game")
    print("\nCongrats! You have been certificate Sokoban King!")

if __name__ == "__main__":
    play()
