# write_data.py

import json
import datetime
import time
import random
import tools

# create data: return time stamp and data
def create_data():
    data        = {}
    fed_numbers = list(range(1000, 1020))
    # get current time
    now         = datetime.datetime.now()
    time_stamp  = now.strftime('%Y-%m-%d %H:%M:%S')
    for fed_num in fed_numbers:
        fed_name                    = "FED_{0:04}".format(fed_num)
        name                        = fed_name
        time                        = time_stamp
        happy_counter               = random.randrange(100)
        sad_counter                 = random.randrange(2)
        middle_of_the_road_counter  = random.randrange(10)
        status_code                 = random.randrange(2)
        data[fed_name] = {
            "name"                          : name,
            "time"                          : time,
            "happy_counter"                 : happy_counter,
            "sad_counter"                   : sad_counter,
            "middle_of_the_road_counter"    : middle_of_the_road_counter,
            "status_code"                   : status_code,
        }
    return time_stamp, data

# write data to json file
def write_data(time_stamp, data, output_file):
    print("{0} | Writing data...".format(time_stamp))
    with open(output_file, "w") as f:
        json.dump(data, f, indent=4, sort_keys=True)

# main
def main():
    output_dir  = "data"
    output_file = "{0}/fed_data.json".format(output_dir)
    tools.makeDir(output_dir)

    # loop parameters
    loop_forever    = True  # choose whether to loop
    delay           = 1.0   # delay time in seconds
    
    if loop_forever:
        # loop forever
        while True:
            time_stamp, fed_data = create_data()
            write_data(time_stamp, fed_data, output_file)
            time.sleep(delay)   # time delay
    else:
        # just write data once
        time_stamp, fed_data = create_data()
        write_data(time_stamp, fed_data, output_file)

if __name__ == '__main__':
    main()

