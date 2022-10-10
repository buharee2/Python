#! /usr/bin/env python3

import os
import requests

files = os.listdir('/data/feedback/')

for file in files:
    with open('/data/feedback/' + file) as information:
        info = information.read().split('\n')
        feedback = {'title':info[0], 'name':info[1], 'date':info[2], 'feedback':info[3]}

        response = requests.post('http://34.123.192.178/feedback/', data = feedback)
        print(response.status_code)