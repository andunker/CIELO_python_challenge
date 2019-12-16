#!./vEnv/bin/python

import json

import requests
import argparse

try:
    parser = argparse.ArgumentParser()
    parser.add_argument('METHOD', choices=[
                        'get', 'post'], help='Request method')
    parser.add_argument('endpoint', help='Request endpoint URI fragment')

    parser.add_argument('-d', '--data', help='Data to send with request')
    parser.add_argument(
        '-o', '--output', help='Output to .json or .csv file (default: dump to stdout)')

    arguments = parser.parse_args()

    if(arguments.METHOD == 'get'):
        response = requests.get(
            'https://jsonplaceholder.typicode.com%s' % arguments.endpoint)

    print(response.text)
except Exception as exception:
    print('Error')
