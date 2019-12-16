#!./vEnv/bin/python

import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('METHOD' ,choices=['get', 'post'], help='Request method')
parser.add_argument('endpoint', help='Request endpoint URI fragment')

parser.add_argument('-d', '--data', help='Data to send with request')
parser.add_argument('-o', '--output', help='Output to .json or .csv file (default: dump to stdout)')
                
parser.parse_args()

print('hello world')

