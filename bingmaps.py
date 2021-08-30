### This script calls Bing Maps API and sends a POST request to get all combinations of destinations and 


import requests
import pprint as pp
import json
import choose_best
import csv

scale_factors = [1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2]

def dma(origin, destination):
    API_KEY = "AiaaVYXhwQiNcMthcNpbYDq6qDRUV90fb1kX1V8YnIQTpB0hhVQMyNKpN0uKngfM"
    # base_url = "https://dev.virtualearth.net/REST/v1/Routes/DistanceMatrix?origins="
    # origins = "47.6044,-122.3345;47.6731,-122.1185;47.6149,-122.1936"
    # url2 = "&destinations="
    # destinations = "42.358965,-83.479666"
    # destinations = "42.3589725,-83.47966869999999;42.32240880000001,-83.4785661;42.322267,-83.48752449999999;42.3191941,-83.4846913;42.3577808,-83.4817915;42.363706,-83.4701917;42.3371613,-83.4784066;42.3376271,-83.459937;42.3222605,-83.4582138;42.3508136,-83.4796495;42.35795969999999,-83.4787328;42.3594353,-83.4643135;42.358645,-83.4591867;42.351332,-83.4598536;42.3070457,-83.4866912;42.307695,-83.4583947;42.3224678,-83.44836920000002;42.3686228,-83.3726992;42.36772939999999,-83.3728036;42.3979358,-83.3536216;42.38377089999999,-83.3527866;42.39844009999999,-83.33399539999999;42.383645,-83.3539139;42.3961683,-83.4024523;42.3970481,-83.4024523;42.397271,-83.35337109999999;42.3820763,-83.3539139;42.3977872,-83.3349351;42.3684027,-83.3520559;42.41306290000001,-83.3355407;42.3983538,-83.31544939999999;42.3989536,-83.3152405;42.3967421,-83.4130899;42.3831615,-83.37363839999999;42.3832339,-83.372574;42.3817905,-83.37229719999999;42.3959352,-83.4133611;42.3680603,-83.4020768;42.3671955,-83.40201429999999;42.411212,-83.3748279;42.4119541,-83.37476529999999;42.3811107,-83.3314829;42.3540364,-83.3521197;42.3464138,-83.3514505;42.3543096,-83.332674;42.347541,-83.331462;42.369184,-83.32501549999999;42.347492,-83.3324501;42.3702605,-83.3139454;42.3380213,-83.3503441;42.3557366,-83.38685509999999;42.344166,-83.38471899999999;42.3388587,-83.36478919999999;42.3384964,-83.38534489999999;42.3525044,-83.4108166;42.36184979999999,-83.4158846;42.3720094,-83.4305026;42.38461179999999,-83.3149689;42.4316809,-83.4294809;42.4239961,-83.4736281;42.4374538,-83.492774"
    # url3 = "&travelMode=driving&distanceUnit=mi&key="

    # url = base_url + origins + url2 + destinations + url3 + API_KEY

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
                        # output_file.write("Origin\n")
                        # output_file.write("Origin Index: " + str(element['originIndex']) + "\n")
                        originIndex = element['originIndex']
                    # output_file.write(str(element['travelDistance']) + "," + str(element['travelDuration']))
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
    
def format(value):
    return "%.5f" % value



# dma(coordinates.get_origins(coordinates.ca), destinations["canton"])