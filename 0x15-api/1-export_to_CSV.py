#!/usr/bin/python3
""" API """
import csv
import requests
import sys


if __name__ == '__main__':
    task = []
    id_user = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/' + id_user + '/todos'
    url_user = 'https://jsonplaceholder.typicode.com/users/' + id_user
    req_user = requests.get(url_user)
    req_user = req_user.json()
    req = requests.get(url)
    req = req.json()

    with open(id_user + '.csv', mode='w') as f:
        write = csv.writer(f, delimiter=',', quotechar='"',
                           quoting=csv.QUOTE_ALL)
        for line in req:
            write.writerow([line['userId'],
                            req_user['username'],
                            line['completed'],
                            line['title']])
