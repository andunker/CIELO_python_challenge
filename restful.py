#!./vEnv/bin/python
import requests

from utils import get_arguments, get_csv_path, get_json_path, make_response, get_api_result, generate_payload

try:

    arguments = get_arguments()

    api_result = get_api_result(arguments.METHOD, arguments.endpoint, arguments.data)

    payload = generate_payload(api_result.json(), arguments.output)

    response = make_response(200, payload)

    print(response)
except Exception as exception:
    print('something went wrong')
