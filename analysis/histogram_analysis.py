import sys
import os
import numpy as np

sys.path.append(os.path.abspath('..'))
from preprocessing import shroom_dealer

def get_hist_data():
    attr_map = shroom_dealer.get_attribute_dictionary()
    df = shroom_dealer.get_data_frame()

    hist_data = dict([(atr,None) for atr in attr_map])
    poison_hist_data = dict([(atr,None) for atr in attr_map])

    for x in attr_map:
        counts = dict([(attr_map[x][y],0) for y in attr_map[x]])
        poison_counts = dict([(attr_map[x][y],0) for y in attr_map[x]])

        for val, poison in zip(df[x],df["poisonous"]):
            counts[attr_map[x][val]]+=1
            if(poison == "p"):
                poison_counts[attr_map[x][val]]+=1
        hist_data[x] = counts
        poison_hist_data[x] = poison_counts

    return hist_data, poison_hist_data

#tf_tpf - Term Frquency to Poison Frequency
def get_tf_tpf():
    data,poison_data = get_hist_data()
    tf_tpf = {}

    for val in data:
        tf_tpf[val] = dict([(x,poison_data[val][x]/data[val][x]) for x in data[val] if data[val][x] != 0])
    return tf_tpf
