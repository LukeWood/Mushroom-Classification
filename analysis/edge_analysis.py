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
            nodes[attr_names[attr][row[attr]]][attr_names[attr2][row[attr2]]] = True

with open("../visualizations/edge-chart/edges.json","w") as f:
    f.write(json.dumps([{"name":x,"imports":[y for y in nodes[x]]} for x in nodes]))
