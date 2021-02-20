import json

# Write your awesome code here
json_input_string = input()
input_list = json.loads(json_input_string)
errors_list = [0, 0, 0, 0, 0, 0, 0]


def checkData(json_string):
    global errors_list
    for dic in json_string:
        if not isinstance(dic['bus_id'], int) or not str(dic['bus_id']):
            errors_list[1] += 1
            errors_list[0] += 1
        if not isinstance(dic['stop_id'], int) or not str(dic['stop_id']):
            errors_list[2] += 1
            errors_list[0] += 1
        if not isinstance(dic['stop_name'], str) or not str(dic['stop_name']):
            errors_list[3] += 1
            errors_list[0] += 1
        if not isinstance(dic['next_stop'], int) or not str(dic['next_stop']):
            errors_list[4] += 1
            errors_list[0] += 1
        if dic['stop_type'] not in ('S', 'O', 'F', ''):
            errors_list[5] += 1
            errors_list[0] += 1
        if not isinstance(dic['a_time'], str) or len(dic['a_time']) != 5:
            errors_list[6] += 1
            errors_list[0] += 1


def printErrorDictionary():
    global errors_list
    error_dictionary = {'Type and required field validation': f'{errors_list[0]} errors',
                        'bus_id': errors_list[1],
                        'stop_id': errors_list[2],
                        'stop_name': errors_list[3],
                        'next_stop': errors_list[4],
                        'stop_type': errors_list[5],
                        'a_time': errors_list[6]}
    for key, value in error_dictionary.items():
        print(key, ': ', value)


def startProgram():
    checkData(input_list)
    printErrorDictionary()


startProgram()


