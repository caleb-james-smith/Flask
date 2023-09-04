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

# print all keys in dictionary with depth
def print_key_depth(input_dict, depth=1):
    for key, value in input_dict.items():
        print("depth {0}: {1}".format(depth, key))
        if isinstance(value, dict):
            print_key_depth(value, depth=depth+1)

# dump json to file with nice formatting
def pretty_dump_json(input_dict, output_file):
    with open(output_file, "w") as f:
        json.dump(input_dict, f, ensure_ascii=False, indent=4)

