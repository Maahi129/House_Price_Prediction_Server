import json
import pickle
import numpy as np

__locations = None
__model = None
__data_columns = None

def get_estimate_price(location,sqft,bhk,bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1
    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bhk
    x[2] = bath
    if loc_index>=0:
        x[loc_index]=1
    return round(__model.predict([x])[0],2)
def get_location_names():
    return  __locations
def load_save_artifacts():
    print("Loading...")
    global __locations
    global __model
    global __data_columns

    with open('./artifacts/columns.json', 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]

    with open('./artifacts/house_price.pickle', 'rb') as f:
        __model = pickle.load(f)
    print("Done...")

if __name__ == '__main__':
    load_save_artifacts()
    print(get_location_names())
    print(get_estimate_price('abbigere',1900,3,3))
