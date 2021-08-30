import csv 
import json
import time

def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray = []
    #read csv file
    with open(csvFilePath, encoding='utf-8') as csvf: 
        #load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf) 

        #convert each csv row into python dict
        for row in csvReader: 
            #add this python dict to json array
            jsonArray.append(row)
  
    # return json.dumps(jsonArray, indent=4)
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf: 
        jsonString = json.dumps(jsonArray, indent=4)
        jsonf.write(jsonString)


# csv_to_json("canton_geocodes.csv", "canton_geocodes.json")
# csv_to_json("nyc_geocodes.csv", "nyc_geocodes.json")
# csv_to_json("la_geocodes.csv", "la_geocodes.json")
# csv_to_json("chicago_geocodes.csv", "chicago_geocodes.json")
# csv_to_json("houston_geocodes.csv", "houston_geocodes.json")

csv_to_json("canton_marathon.csv", "canton_marathon.json")
csv_to_json("canton_bp.csv", "canton_bp.json")
csv_to_json("canton_exxonmobil.csv", "canton_exxonmobil.json")
csv_to_json("canton_shell.csv", "canton_shell.json")
csv_to_json("canton_sunoco.csv", "canton_sunoco.json")
