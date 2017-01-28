from sklearn.preprocessing import OneHotEncoder
import pandas

attribute_names = [x.split(":")[0] for x in open("../raw_data/descriptors.txt")]

df = pandas.read_csv("../raw_data/agaricus-lepiota.data.txt",names=attribute_names)
