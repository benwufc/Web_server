import requests
#import numpy as np
import argparse
import json

parse = argparse.ArgumentParser()
parse.add_argument('--a', type=int)
parse.add_argument('--b', type=int)
parse.add_argument('--o', type=str)
args = parse.parse_args()
data = {'a':args.a,'b':args.b}

addr = 'http://localhost:6000'
test_url = addr + '/api/' + args.o
content_type = 'application/json'
headers = {'content-type': content_type}

response = requests.post(test_url, json=json.dumps(data), headers=headers)
print(response.text)
