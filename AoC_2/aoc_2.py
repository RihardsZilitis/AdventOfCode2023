import sys
import re

infile = sys.path[0] + "\input.txt"

with open(infile, "r") as f:
    lines = [line.strip() for line in f.readlines()]
    min_cubes_for_game = []

    for line in lines:
        game = line.split(": ")[0]
        game_id = game.split(" ")[1]
        game_results = line.strip().split(": ")[1].replace("; ", ";").replace(", ", ",").replace(" ", "=")
        cubes_needed = {
            'red'   : '0',
            'green' : '0',
            'blue'  : '0'
        }
        for game_result in game_results.split(";"):
            game_result = game_result.strip()
            this_game = list(result.split("=") for result in game_result.split(","))
            this_game = dict([[result[1], result[0]] for result in this_game])

            for this_game_cube, this_game_count in sorted(this_game.items()):
                for cube, count in sorted(cubes_needed.items()):
                    if cube == this_game_cube and int(this_game_count) > int(count):
                        cubes_needed[cube] = int(this_game_count)

        if game not in min_cubes_for_game:
            min_cubes_for_game.append([game, cubes_needed])

    sum_of_power = 0

    for game in min_cubes_for_game:
        power = 1
        for cubes in game:
            if isinstance(cubes, dict):
                for point in cubes.values():
                    power = power * point
                sum_of_power = sum_of_power + power

    print(sum_of_power)