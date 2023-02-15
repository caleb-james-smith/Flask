# write_data.py

import tools
import json

# create data
def create_data():
    data = {}
    fed_numbers = list(range(1000, 1020))
    for fed_num in fed_numbers:
        fed_name                    = "FED_{0:04}".format(fed_num)
        name                        = fed_name
        time                        = 0
        happy_counter               = 0
        sad_counter                 = 0
        middle_of_the_road_counter  = 0
        status_code                 = 0
        data[fed_name] = {
            "name"                          : name,
            "time"                          : time,
            "happy_counter"                 : happy_counter,
            "sad_counter"                   : sad_counter,
            "middle_of_the_road_counter"    : middle_of_the_road_counter,
            "status_code"                   : status_code,
        }
    return data

# write data to json file
def write_data(data, output_file):
    print("Writing data...")
    with open(output_file, "w") as f:
        json.dump(data, f, indent=4, sort_keys=True)

# main
def main():
    output_dir  = "data"
    output_file = "{0}/fed_data.json".format(output_dir)
    fed_data    = create_data()
    tools.makeDir(output_dir)
    write_data(fed_data, output_file)

if __name__ == '__main__':
    main()

