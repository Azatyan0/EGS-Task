""" The "Reader" class was created for the conversion of JSON data to a dictionary
    Where the dictionary's keys are input strings and values are the "Result" class objects.
"""

import json
from EGS_task.Result import Result


class Reader:
    # Opening JSON file
    @staticmethod
    def json2dict(json_path):
        with open(json_path) as json_file:
            data = json.load(json_file)

        input_dct = {}

        for i in range(len(data)):
            result = Result()
            result.expected_res_setter(data[i]["result"]["expected"])
            input_dct[data[i]["key"]] = result

        return input_dct
