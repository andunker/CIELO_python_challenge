import json
import csv
import os

import requests
import argparse


def get_arguments():

    parser = argparse.ArgumentParser()
    parser.add_argument('METHOD', choices=[
                        'get', 'post'], help='Request method')
    parser.add_argument('endpoint', help='Request endpoint URI fragment')

    parser.add_argument('-d', '--data', help='Data to send with request')
    parser.add_argument(
        '-o', '--output', help='Output to .json or .csv file (default: dump to stdout)')

    arguments = parser.parse_args()
    return arguments


def generate_payload(api_result, file_extension):

    payload = api_result

    if(file_extension):

        if(file_extension.split('.')[1] == 'csv'):
            payload = get_csv_path(api_result, file_extension)

        if(file_extension.split('.')[1] == 'json'):
            payload = get_json_path(api_result, file_extension)

    return payload


def get_api_result(method, endpoint):
    api_result = requests.get(
        'https://jsonplaceholder.typicode.com%s' % endpoint)
    return api_result


def get_csv_path(payload, file_name):
    csv_columns = ['userId', 'id', 'title', 'body']

    with open(file_name, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in payload:
            writer.writerow(data)

    csv_path = os.getcwd() + '/%s' % file_name
    return(csv_path)


def get_json_path(payload, file_name):
    with open(file_name, 'w') as jsonfile:
        json.dump(payload, jsonfile)

    json_path = os.getcwd() + '/%s' % file_name
    return(json_path)


def make_response(status_code, payload):
    response = {
        'statusCode': status_code,
        'body': payload
    }
    return json.dumps(response)
