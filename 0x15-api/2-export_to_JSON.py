#!/usr/bin/python3
""" API """
import csv
import json
import requests
import sys


if __name__ == '__main__':
    dic = {}
    lis = []
    id_user = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/' + id_user + '/todos'
    url_user = 'https://jsonplaceholder.typicode.com/users/' + id_user
    req_user = requests.get(url_user)
    req_user = req_user.json()
    req = requests.get(url)
    req = req.json()

    for line in req:
        dic['task'] = line['title']
        dic['completed'] = line['completed']
        dic['username'] = req_user['username']
        lis.append(dic)

    with open(id_user + '.json', mode='w') as f:
        json.dump({id_user: lis}, f)
