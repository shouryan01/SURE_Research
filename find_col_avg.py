### This script reads in data from simulation_results.csv (which bingmaps.py writes to) and then summarizes the data by the mean of the column and then writes it to coordinate_points


import pandas as pd
import csv
import choose_best

scale_factors = [1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2]

columns = [
    "shortest_distance","shortest_time",
    "small_sedan_distance", "small_sedan_time",
    "med_sedan_distance", "med_sedan_time",
    "large_sedan_distance", "large_sedan_time",
    "small_suv_distance", "small_suv_time",
    "med_suv_distance", "med_suv_time",
    "minivan__distance", "minivan_time"
    "pickup_distance", "pickup_time"  
]

def find_avg():
    data = pd.read_csv("simulation_results.csv", header = None)
    data = data.mean().tolist()
    with open("simulation_points.csv", "a") as file:
        writer = csv.writer(file, delimiter=',', escapechar=' ', quoting=csv.QUOTE_NONE)
        writer.writerow(data)

    # clears the file to get new avg data
    with open("simulation_results.csv", "w+"):
        pass

# find_avg()