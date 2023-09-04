# dump_data.py

import tools

def run():
    input_file  = "data/FEDMonitor_2023_09_01_v2.json"
    output_file = "data/FEDMonitor_2023_09_01_v2_pretty.json"
    data = tools.load_data(input_file)
    tools.pretty_dump_json(data, output_file)

def main():
    run()

if __name__ == '__main__':
    main()

