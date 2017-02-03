import json
import sys
import os
sys.path.append(os.path.abspath('..'))

from preprocessing import shroom_dealer

attr_names= shroom_dealer.get_attribute_dictionary()

nodes = {}

df = shroom_dealer.get_data_frame()

for index, row in df.iterrows():
    for attr in attr_names:
        attr_id = attr+"-"+attr_names[attr][row[attr]]

        for attr2 in attr_names:
            if(attr == attr2):
                continue

            attr_id2 = attr2+"-"+attr_names[attr2][row[attr2]]

            if(attr_id not in nodes):
                nodes[attr_id] = {}
            if(attr_id2 not in nodes[attr_id]):
                nodes[attr_id][attr_id2] = 0

            nodes[attr_id][attr_id2]+=1

for MIN in range(0,159):
    with open("../visualizations/edge-chart/edge_data/edges%d.json" % (MIN*25),"w") as f:
        f.write(json.dumps([{"name":x,"imports":[y for y in nodes[x] if nodes[x][y] >= MIN*25*2]} for x in nodes]))
