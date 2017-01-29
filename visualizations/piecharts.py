import sys
import os

import numpy as np
import matplotlib.pyplot as plt

sys.path.append(os.path.abspath('..'))
from analysis import piecharts_analysis
from visualizations import comparative_plots
from preprocessing import shroom_dealer

data,poison_data = piecharts_analysis.get_pie_data()

tf_tpf = {}

a_map = shroom_dealer.get_attribute_dictionary()
df = shroom_dealer.get_data_frame()

fig, ax = plt.subplots()

colors = ["#E13F29", "#D69A80", "#D63B59", "#AE5552", "#CB5C3B", "#EB8076", "#96624E"]
for val in data:
    edData = comparative_plots.data(val)["edible"]
    poData = comparative_plots.data(val)["poisonous"]
    labels = shroom_dealer.get_attribute_dictionary()[val]

    plt.pie(list(edData.values()), labels=list(labels.values()), shadow=False, colors=colors, startangle=90, autopct='%1.1f%%')
    plt.title("Edible relation with %s" % (val))
    plt.savefig('piecharts/%s-Edible.png' % (val), dpi=fig.dpi)
    plt.close()

    plt.pie(list(poData.values()), labels=list(labels.values()), shadow=False, colors=colors, startangle=90, autopct='%1.1f%%')
    plt.title("Poisonous relation with %s" % (val))
    plt.savefig('piecharts/%s-Poison.png' % (val), dpi=fig.dpi)
    plt.close()
