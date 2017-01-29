import sys
import os

sys.path.append(os.path.abspath('..'))
from preprocessing import shroom_dealer

def get_pie_data():
    att_map = shroom_dealer.get_attribute_dictionary()
    df = shroom_dealer.get_data_frame()

    pie_data = dict([(atr,None) for atr in att_map])
    poison_pie_data = dict([(atr,None) for atr in att_map])

    for x in att_map:
        counts = dict([(att_map[x][y],0) for y in att_map[x]])
        poison_counts = dict([(att_map[x][y],0) for y in att_map[x]])

        for val, poison in zip(df[x],df["poisonous"]):
            counts[att_map[x][val]]+=1
            if(poison == "p"):
                poison_counts[att_map[x][val]]+=1
        pie_data[x] = counts
        poison_pie_data[x] = poison_counts

    return pie_data, poison_pie_data
