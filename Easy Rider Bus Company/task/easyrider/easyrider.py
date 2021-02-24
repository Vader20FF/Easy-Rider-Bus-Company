import json
import sys

json_input_string = input()
input_list = json.loads(json_input_string)
bus_stops_names_on_demand = []


def checkData(json_string):
    global bus_stops_names_on_demand

    for dic in json_string:
        if dic['stop_type'] == 'O' and dic['stop_name'] not in ['Fifth Avenue', 'Sesame Street', 'Bourbon Street',
                                                                'Pilotow Street', 'Prospekt Avenue']:
            bus_stops_names_on_demand.append(dic['stop_name'])


def printResult():
    print("On demand stops test:")
    if bus_stops_names_on_demand:
        print("Wrong stop type: ", sorted(bus_stops_names_on_demand))
    else:
        print("OK")


def startProgram():
    checkData(input_list)
    printResult()


startProgram()
