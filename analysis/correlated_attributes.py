import sys
import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sys.path.append(os.path.abspath('..'))
from preprocessing import shroom_dealer

df = shroom_dealer.get_data_frame()
attr_dict = shroom_dealer.get_attribute_dictionary()

data = []
for attribute in attr_dict:
    for sub_attr in attr_dict[attribute]:
        data.append((attr_dict[attribute][sub_attr],[1 if x==sub_attr else 0 for x in df[attribute]]))

l = [x[1] for x in data]

corr_df = pd.DataFrame(np.array(l).transpose(), columns=[x[0] for x in data]).corr().dropna(thresh=1).drop("distant")

fig, ax = plt.subplots(figsize=(20,20))

sns.heatmap(corr_df)
fig.autofmt_xdate()

locs, labels = plt.yticks()
plt.setp(labels,rotation=45)

plt.show()
