import json
import sys

json_input_string = input()
input_list = json.loads(json_input_string)
bus_lines_with_wrong_time = {}
bus_lines_numbers_with_wrong_time = set()


def checkData(json_string):
    global bus_lines_with_wrong_time
    smallest_time = "00:00"
    current_bus_id = 128

    for dic in json_string:
        if dic['bus_id'] in bus_lines_numbers_with_wrong_time:
            continue
        if dic['bus_id'] != current_bus_id:
            smallest_time = "00:00"
            current_bus_id = dic['bus_id']
        if dic['a_time'] < smallest_time:
            bus_lines_numbers_with_wrong_time.add(dic['bus_id'])
            bus_lines_with_wrong_time[dic['bus_id']] = dic['stop_name']
        smallest_time = dic['a_time']


def printResult():
    global bus_lines_with_wrong_time
    print("Arrival time test:")
    if bus_lines_with_wrong_time:
        for bus_line, station in bus_lines_with_wrong_time.items():
            print("bus_id line " + f'{bus_line}: wrong time on station {station}')
    else:
        print("OK")


def startProgram():
    checkData(input_list)
    printResult()


startProgram()
