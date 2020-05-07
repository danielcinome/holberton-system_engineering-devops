#!/usr/bin/python3
""" Request Reddit API """
import requests


def top_ten(subreddit):
    """ Top Ten """
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    tok = {'user-agent': 'X-Modhash'}
    req = requests.get(url, headers=tok)
    if req.history or req.status_code == 404:
        print('None')
    else:
        req = req.json()
        req = req.get('data').get('children')
        for title in req:
            print(title.get('data').get('title'))
