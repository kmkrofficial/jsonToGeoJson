#! usr/bin/env python

from sys import argv
from os.path import exists
import simplejson as json 

in_file = input("Enter the name of the Json File that needs to be converted: ")
out_file = input("Enter the name of the Output File: ")
data = json.load(open(in_file))

geojson = {
    "type": "FeatureCollection",
    "features": [
    {
        "type": "Feature",
        "geometry" : {
            "type": "Point",
            "coordinates": [d["lon"], d["lat"]],
            },
        "properties" : d,
     } for d in data]
}


output = open(out_file, 'w')
json.dump(geojson, output)

print ("Success... Check the same folder where this program is saved.")
