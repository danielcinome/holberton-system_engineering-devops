#!/usr/bin/python3
""" API """
import requests
import sys

if __name__ == '__main__':
    task = []
    count = 0
    id_user = sys.argv[1]
    url_user = 'https://jsonplaceholder.typicode.com/users/' + id_user
    req_user = requests.get(url_user)
    param = {'userId': id_user}
    req_todo = requests.get('https://jsonplaceholder.typicode.com/todos/',
                            params=param)
    req_user = req_user.json()
    req_todo = req_todo.json()
    for value in req_todo:
        if value['completed'] is True:
            count += 1
            task.append(value['title'])
    print('Employee {} is done with tasks({}/{}):'.format(
          req_user['name'],
          count,
          len(req_todo)))
    for val in task:
        print(' \t{}'.format(val))
