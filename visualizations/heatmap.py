import sys
import os

import numpy as np
import matplotlib.pyplot as plt

sys.path.append(os.path.abspath('..'))
from analysis import piecharts_analysis
from visualizations import comparative_plots
from preprocessing import shroom_dealer

data,poison_data = piecharts_analysis.get_pie_data()

a_map = shroom_dealer.get_attribute_dictionary()
df = shroom_dealer.get_data_frame()


#Stacked Bar Graph
# the cross tab operator provides an easy way to get these numbers
#poison = pd.crosstab([df['population'],df['habitat'] ],
#                       df.poisonous.astype(str))
#poison.plot(kind='barh', stacked=True)
#plt.show()
