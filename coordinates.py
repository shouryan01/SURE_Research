import random
import json
# lat_max, lat_min, long_min, long_max

ny = [40.88, 40.58152, -73.65966, -74.0919]
la = [34.1831, 33.84693, -118.07492, -118.42579]
ch = [41.96905, 41.63942, -87.5268, -87.92902]
ho = [29.94623, 29.59099, -95.13771, -95.57167]
px = [33.68342, 33.28024, -111.87903, -112.27591]

wc = []
ta = []
pp = []
cn = []
wj = []

ca = [42.38866, 42.24861, -83.3501, -83.56503]


lat_max = 42.4744 #y_min
lat_min = 42.19625 #y_max
long_max = -83.67491 #x_min 
long_min = -83.27229 #x_max

def make_random_point(lat_max, lat_min, long_min, long_max):
    lat = lat_max + (random.random() * (lat_min - lat_max)); 
    long = long_max + (random.random() * (long_min - long_max))
    # return str(lat) + "," + str(long)
    return (lat, long)

def get_origins(bounds, s):
    random.seed(s)
    coords = []
    for i in range(10):
        coords.append(make_random_point(*bounds))
    return json.dumps([{'latitude': lats, 'longitude': longs} for lats, longs in coords])

# gmaps.dma(*get_random_points(*ca))

# get_random_points(*ca)
# get_random_points(*ca)