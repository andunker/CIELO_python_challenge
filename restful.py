#!./vEnv/bin/python
import requests

from utils import get_arguments, get_csv_path, get_json_path, make_response, get_api_result

try:

    arguments = get_arguments()

    api_result = get_api_result(arguments.METHOD, arguments.endpoint)

    payload = api_result.json()

    if(arguments.output):

        if(arguments.output.split('.')[1] == 'csv'):
            payload = get_csv_path(payload, arguments.output)

        if(arguments.output.split('.')[1] == 'json'):
            payload = get_json_path(payload, arguments.output)

    status_code = 200

    response = make_response(200, payload)

    print(response)
except Exception as exception:
    print('something went wrong')
