### This script runs the simulation, calling all the other assistor scripts


import bingmaps
import find_col_avg
import coordinates
import time

## these are parameters that are passed into bingmaps, which are then in turn passed to choose_best.py which uses these parameters to "choose the best" option
scale_factors = [1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2]
# scale_factors = [1, 1.05, 1.1, 1.15, 1.2, 1.25, 1.3, 1.35, 1.4, 1.45, 1.5, 1.55, 1.6, 1.65, 1.7, 1.75, 1.8, 1.85, 1.9, 1.95, 2]

## choose which city's gas stations are "destinations"
destinations = {
    "canton": "canton_geocodes.json",
    "nyc": "nyc_geocodes.json",
    "la": "la_geocodes.json",
    "chicago": "chicago_geocodes.json",
    "houston": "houston_geocodes.json",
    "phoenix": "",
    "wichita": "",
    "tacoma": "",
    "pp": "",
    "charleston": "",
    "wjordan": ""
}

## choose which brand of gas stations (canton) are "destinations"
price_destinations = {
    "marathon": "canton_marathon.json",
    "bp": "canton_bp.json",
    "shell": "canton_shell.json",
    "exxonmobil": "canton_exxonmobil.json",
    "sunoco": "canton_sunoco.json",
}

## choose what density (10-100%) of gas stations (canton) are "destinations"
file_names = ["canton_geocodes_1.json",
    "canton_geocodes_2.json",
    "canton_geocodes_3.json",
    "canton_geocodes_4.json",
    "canton_geocodes_5.json",
    "canton_geocodes_6.json",
    "canton_geocodes_7.json",
    "canton_geocodes_8.json",
    "canton_geocodes_9.json",
    "canton_geocodes_10.json"
]

## avg of 100 random points to simulation_results.csv
# def start():
#     for i in range(11):
#         for j in range(10):
#             bingmaps.dma(coordinates.get_origins(coordinates.ca), destinations["canton"], i)
#             time.sleep(2)
#         find_col_avg.find_avg()

## avg of brand outcomes
def start():
    for i in range(10):
        bingmaps.dma(coordinates.get_origins(coordinates.ca, i), price_destinations["exxonmobil"])
        time.sleep(2) # done so as to not overload the bing maps api
        find_col_avg.find_avg()

start()