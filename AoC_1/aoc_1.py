import sys
import re

infile = sys.path[0] + "\input.txt"

text_to_number = {
    'zero' : '0',
    'one'  : '1',
    'two'  : '2',
    'three': '3',
    'four' : '4',
    'five' : '5',
    'six'  : '6',
    'seven': '7',
    'eight': '8',
    'nine' : '9'
}

with open(infile, "r") as f:
    calibrations = [line.strip() for line in f.readlines()]
    calibrations_clean = []

    for calibration in calibrations:
        matches = re.findall(r'(?=(1|2|3|4|5|6|7|8|9|0|zero|one|two|three|four|five|six|seven|eight|nine))', calibration)

        for idx, match in enumerate(matches):
            for key, value in text_to_number.items():
                if match == key:
                    matches[idx] = matches[idx].replace(match, value)

        values = ''.join(character for character in matches if character.isdigit())
        calibrations_clean.append(values[0] + values[-1])

    print(sum([int(value) for value in calibrations_clean]))