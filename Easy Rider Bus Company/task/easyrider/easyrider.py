import json
import sys

json_input_string = input()
input_list = json.loads(json_input_string)
startStops = set()
transferStops = set()
finishStops = set()


def checkData(json_string):
    stops = {128: {'start_stop': False, 'finish_stop': False}, 256: {'start_stop': False, 'finish_stop': False},
             512: {'start_stop': False, 'finish_stop': False}}
    transferStopsCounter = {"Sesame Street": 0, "Fifth Avenue": 0, "Prospekt Avenue": 0, "Elm Street": 0,
                            "Sunset Boulevard": 0, "Bourbon Street": 0, "Pilotow Street": 0, "Abbey Road": 0,
                            "Santa Monica Boulevard": 0, "Beale Street": 0, "Startowa Street": 0, "Lombard Street": 0,
                            "Orchard Road": 0, "Khao San Road": 0, "Michigan Avenue": 0, "Arlington Road": 0,
                            "Niebajka Avenue": 0, "Jakis Street": 0, "Jakas Avenue": 0, "Karlikowska Avenue": 0,
                            "Parizska Street": 0}
    currentBusLines = set()
    global startStops, transferStops, finishStops
    for dic in json_string:
        # Checking transfer stops
        if dic['stop_name'] in transferStopsCounter:
            transferStopsCounter[dic['stop_name']] += 1
        if transferStopsCounter[dic['stop_name']] > 1:
            transferStops.add(dic['stop_name'])

        # Checking start stops
        if dic['stop_type'] == 'S':
            startStops.add(dic['stop_name'])
            if dic['bus_id'] == 128:
                stops[128]['start_stop'] = True
            elif dic['bus_id'] == 256:
                stops[256]['start_stop'] = True
            else:
                stops[512]['start_stop'] = True

        # Checking final stops
        elif dic['stop_type'] == 'F':
            finishStops.add(dic['stop_name'])
            if dic['bus_id'] == 128:
                stops[128]['finish_stop'] = True
            elif dic['bus_id'] == 256:
                stops[256]['finish_stop'] = True
            else:
                stops[512]['finish_stop'] = True
        currentBusLines.add(dic['bus_id'])

    for bus_line, stops in stops.items():
        if bus_line not in currentBusLines:
            continue
        for stopCheck in stops:
            if not stops[stopCheck]:
                print("There is no start or end stop for the line:", bus_line)
                sys.exit()

    # for key, value in transferStopsCounter.items():
    #     print(key, value)


def printStops():
    global startStops, transferStops, finishStops
    print("Start stops:", len(startStops), list(sorted(startStops)))
    print("Transfer stops:", len(transferStops), list(sorted(transferStops)))
    print("Finish stops:", len(finishStops), list(sorted(finishStops)))


def startProgram():
    checkData(input_list)
    printStops()




startProgram()
