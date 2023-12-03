import sys
import re

infile = sys.path[0] + "\input.txt"

bag = {
    'red'   : '12',
    'green' : '13',
    'blue'  : '14'

}

with open(infile, "r") as f:
    lines = [line.strip() for line in f.readlines()]
    impossible_games = []
    possible_games = []

    for line in lines:
        game = line.split(": ")[0]
        game_id = game.split(" ")[1]
        game_results = line.split(": ")[1]

        for game_result in game_results.split(";"):
            this_game = dict(result.split(" ") for result in game_result.strip().split(", "))
            possible_game = 1

            for count, cube in this_game.items():
                if possible_game:
                    for allowed_cube, allowed_count in bag.items():
                        if cube == allowed_cube and int(count) > int(allowed_count):
                            if game.split(" ")[1] not in impossible_games:
                                impossible_games.append(game_id)
                            possible_game = 0
                            break
        if game_id not in impossible_games:
            possible_games.append(game_id)

    print(sum(int(game) for game in possible_games))