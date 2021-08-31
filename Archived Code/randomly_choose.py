### this script takes all the available gas station data (json format) and returns 10 files with randomly chosen gas stations with probability of being included ranging from 10-100%


import json
import random
import pprint

probability = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
file_names = ["canton_geocodes_1.json",
"canton_geocodes_2.json",
"canton_geocodes_3.json",
"canton_geocodes_4.json",
"canton_geocodes_5.json",
"canton_geocodes_6.json",
"canton_geocodes_7.json",
"canton_geocodes_8.json",
"canton_geocodes_9.json",
"canton_geocodes_10.json"]

with open("canton_geocodes.json") as file:
    data = json.load(file)

selection = []

for trial in range(10):
    with open(file_names[trial], 'w') as file:
        for i in data:
            if random.random() < probability[trial]:
                selection.append(i)
        json.dump(selection, file, indent = 4)
        selection = []