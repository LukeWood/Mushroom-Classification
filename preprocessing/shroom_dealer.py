from sklearn.preprocessing import OneHotEncoder
import pandas

def get_attribute_dictionary():
    # Loads from the descriptors file all attributes w/ mapping to their mappings
    attr_dict = dict([(x.split(":")[0],dict([[y.split("=")[1].strip(),y.split("=")[0].strip()] for y in x.split(":")[1].split(",")])) for x in open("../raw_data/descriptors.txt")])
    return attr_dict

def get_data_frame():
    attribute_names = [x.split(":")[0] for x in open("../raw_data/descriptors.txt")]
    df = pandas.read_csv("../raw_data/agaricus-lepiota.data.txt",names=attribute_names)

    for col in df.columns:
        df[col] = df[col].astype('category')

    return df
