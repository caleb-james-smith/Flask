# tools.py

import os
import json

# creates directory if it does not exist
def makeDir(dir_name):
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

# load data from input json file
def load_data(input_file):
    with open(input_file, "r") as f:
        data = json.load(f)
    return data

