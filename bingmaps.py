### This script calls Bing Maps API and sends a POST request to get all combinations of destinations and origins
### it then writes that data to appropriate simulation.csv file and the best results are written to simulation_results.csv (canton)


import requests
import pprint as pp
import json
import choose_best
import csv


scale_factors = [1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2]

def dma(origin, destination):
    API_KEY = "AiaaVYXhwQiNcMthcNpbYDq6qDRUV90fb1kX1V8YnIQTpB0hhVQMyNKpN0uKngfM"
    post_url = "https://dev.virtualearth.net/REST/v1/Routes/DistanceMatrix?key=" + API_KEY

    json_destinations = json.load(open(destination))
    
    # output = requests.get(url).json()
    output = requests.post(post_url, json = {
        "origins": json.loads(origin),
        "destinations": json_destinations,
        "travelMode": "driving",
        "distanceUnit": "mi"
    }).json()

    pp.pprint(output)
    originIndex = -1

    with open("canton_simulation.csv", 'w') as output_file:
        w = csv.writer(output_file, quoting=csv.QUOTE_NONE)
        for obj in output['resourceSets']:
            for data in obj['resources']:
                for element in data["results"]:
                    if element['originIndex'] > originIndex:
                        w.writerow(["Origin"])
                        w.writerow(["Origin Index: " + str(element['originIndex'])])
                        originIndex = element['originIndex']
                    row = [element['travelDistance'], element['travelDuration']]
                    w.writerow(row)

                    # output_file.write("\n")
                    # print(element['travelDistance'], element['travelDuration'])
        # output_file.write("end")
        w.writerow(["end"])
    
    # flat_result = [item for sublist in result for item in sublist]

    # with open("simulation_results.csv", "a") as file:
    #     writer = csv.writer(file, delimiter=',', escapechar=' ', quoting=csv.QUOTE_NONE)
    #     writer.writerow(flat_result)

    result = choose_best.find_best()

    with open("simulation_results.csv", "a") as file:
        writer = csv.writer(file, delimiter=',', escapechar=' ', quoting=csv.QUOTE_NONE)
        writer.writerow(result)    