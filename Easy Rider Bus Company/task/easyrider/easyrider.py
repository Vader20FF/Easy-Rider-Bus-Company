import json
import re

json_input_string = input()
input_list = json.loads(json_input_string)
errors_list = [0, 0, 0, 0]


def checkData(json_string):
    global errors_list
    for dic in json_string:
        if not re.match(r'[A-Z][a-z]+\s?[A-Z]?[a-z]+?\s(Avenue|Street|Road|Boulevard)$', dic['stop_name']):
            errors_list[1] += 1
            errors_list[0] += 1
        if dic['stop_type'] not in ['S', 'O', 'F', '']:
            errors_list[2] += 1
            errors_list[0] += 1
        if not re.match(r'[0-2][0-9]:[0-5][0-9]$', dic['a_time']):
            errors_list[3] += 1
            errors_list[0] += 1


def printErrorDictionary():
    global errors_list
    error_dictionary = {'Format validation': f'{errors_list[0]} errors',
                        'stop_name': errors_list[1],
                        'stop_type': errors_list[2],
                        'a_time': errors_list[3]}
    for key, value in error_dictionary.items():
        print(key, ': ', value)


def startProgram():
    checkData(input_list)
    printErrorDictionary()


startProgram()
