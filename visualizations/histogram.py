import sys
import os

sys.path.append(os.path.abspath('..'))
from analysis import histogram_analysis

import matplotlib.pyplot as plt

data,poison_data = histogram_analysis.get_hist_data()
