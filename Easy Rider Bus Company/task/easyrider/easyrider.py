import json
import re

json_input_string = input()
input_list = json.loads(json_input_string)
lineNames = []
numberOfStops = [0, 0, 0, 0]


def checkData(json_string):
    global lineNames
    global numberOfStops
    for dic in json_string:
        if dic['bus_id'] == 128:
            numberOfStops[0] += 1
            if dic['bus_id'] not in lineNames:
                lineNames.append(dic['bus_id'])
        elif dic['bus_id'] == 256:
            numberOfStops[1] += 1
            if dic['bus_id'] not in lineNames:
                lineNames.append(dic['bus_id'])
        elif dic['bus_id'] == 512:
            numberOfStops[2] += 1
            if dic['bus_id'] not in lineNames:
                lineNames.append(dic['bus_id'])
        else:
            numberOfStops[3] += 1
            if dic['bus_id'] not in lineNames:
                lineNames.append(dic['bus_id'])


def printErrorDictionary():
    global lineNames
    global numberOfStops
    print("Line names and number of stops:")
    for index in range(len(lineNames)):
        print("bus_id:", lineNames[index], ", stops:", numberOfStops[index])


def startProgram():
    checkData(input_list)
    printErrorDictionary()


startProgram()
