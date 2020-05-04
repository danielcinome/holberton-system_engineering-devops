#!/usr/bin/python3
""" API """
import csv
import json
import requests
import sys


if __name__ == '__main__':
    dic = {}
    dic_dic = {}
    lis = []
    for id_user in range(1, 11):
        url = 'https://jsonplaceholder.typicode.com/users/' +\
              str(id_user) + '/todos'
        url_user = 'https://jsonplaceholder.typicode.com/users/' + str(id_user)
        req_user = requests.get(url_user)
        req = requests.get(url)
        req_user = req_user.json()
        req = req.json()

        for line in req:
            dic['username'] = req_user['username']
            dic['task'] = line['title']
            dic['completed'] = line['completed']
            lis.append(dic)
            dic = {}
        dic_dic[id_user] = lis

    with open('todo_all_employees.json', mode='w') as f:
        json.dump(dic_dic, f)
