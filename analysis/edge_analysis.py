import json
import sys
import os
sys.path.append(os.path.abspath('..'))

from preprocessing import shroom_dealer

attr_names= shroom_dealer.get_attribute_dictionary()

nodes = {}
for x in attr_names:
    for y in attr_names[x]:
        nodes[attr_names[x][y]] = {}

df = shroom_dealer.get_data_frame()

for index, row in df.iterrows():
    for attr in attr_names:
        for attr2 in attr_names:
            if(attr == attr2):
                continue
            if(attr_names[attr2][row[attr2]] not in nodes[attr_names[attr][row[attr]]]):
                nodes[attr_names[attr][row[attr]]][attr_names[attr2][row[attr2]]] = 0
            nodes[attr_names[attr][row[attr]]][attr_names[attr2][row[attr2]]]+=1

for MIN in range(0,250):
    with open("../visualizations/edge-chart/edge_data/edges%d.json" % (MIN*25),"w") as f:
        f.write(json.dumps([{"name":x,"imports":[y for y in nodes[x] if nodes[x][y] >= MIN*25]} for x in nodes]))
