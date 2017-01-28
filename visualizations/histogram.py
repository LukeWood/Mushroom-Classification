import sys
import os

sys.path.append(os.path.abspath('..'))

from analysis import histogram_analysis

import matplotlib.pyplot as plt

data,poison_data = histogram_analysis.get_hist_data()

tf_tpf = {}

for val in data:
    tf_tpf[val] = dict([(x,poison_data[val][x]/data[val][x]) for x in data[val] if data[val][x] != 0])

all_corrs =[]

for key in tf_tpf:
    for x in tf_tpf[key]:
        all_corrs.append((x,tf_tpf[key][x]))

all_corrs = sorted(all_corrs, key=lambda x: x[1])
print(all_corrs)
