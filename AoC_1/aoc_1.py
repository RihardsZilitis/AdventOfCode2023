import sys

infile = sys.path[0] + "\input.txt"

with open(infile, "r") as f:
    calibrations = [line.strip() for line in f.readlines()]
    calibrations_clean = []

    for calibration in calibrations:
        values = ''.join(character for character in calibration if character.isdigit())
        calibrations_clean.append(values[0] + values[-1])

    print(sum([int(value) for value in calibrations_clean]))