### attemped distance matrix calculation using Google Maps, however it was abandoned because the limit was only 100 origin-destination pairs
### development was moved to bing maps because it allows for 2500 pairs


import requests
import pprint as pp

def dma(lat, long):
    API_KEY = 'AIzaSyAzhNVu-JlgdF3PTKM2Q9jOlap_069BWtw'
    base_url =  'https://maps.googleapis.com/maps/api/distancematrix/json?origins='
    # origin = str(lat) + ", " + str(long)
    origin = "42.31591701274556, -83.50392541175879|42.286232599875, -83.43691351853839"
    url2 = '&destinations='
    destination = ""
    url3 = '&mode=car&key='

    url = base_url + origin + url2 + destination + url3 + API_KEY

    output = requests.get(url).json()
    pp.pprint(output)

    # for obj in output['rows']:
    #     for data in obj['elements']:
    #         print(data['distance']['value'] * 0.000621371)
    #         print(data['duration']['value'] * 0.01666666666)


dma(42.32678789834478, -83.4603281381267)
