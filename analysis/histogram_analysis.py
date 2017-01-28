import sys
import os
import numpy as np

sys.path.append(os.path.abspath('..'))
from preprocessing import shroom_dealer

attr_map = shroom_dealer.get_attribute_dictionary()
df = shroom_dealer.get_data_frame()

hist_data = dict([(atr,None) for atr in attr_map])

for x in attr_map:
    counts = dict([(attr_map[x][y],0) for y in attr_map[x]])
    for row in df[x]:
        counts[attr_map[x][row]]+=1
    hist_data[x] = dict([(c,counts[c]/df.shape[0]) for c in counts])

print(hist_data)
