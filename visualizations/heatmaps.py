import sys
import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sys.path.append(os.path.abspath('..'))
from preprocessing import shroom_dealer

def heatmap_p_vs_e(attribute):
    df = shroom_dealer.get_data_frame()
    labels = shroom_dealer.get_attribute_dictionary()[attribute]
    p_data = df[attribute][df['poisonous'] == 'p'].value_counts()
    e_data = df[attribute][df['poisonous'] == 'e'].value_counts()
    data = pd.concat([p_data, e_data], axis=1)
    data.columns = ['poisonous', 'edible']

    ticks = [labels[a] for a in data.index]

    sns.heatmap(data, annot=True, yticklabels=ticks, fmt='g')

    plt.yticks(rotation=0)
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    heatmap_p_vs_e('odor')
